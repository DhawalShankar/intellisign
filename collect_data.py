# collect_data.py

import cv2
import mediapipe as mp
import csv
import os

# Constants
CSV_FILE = "data/gesture_data.csv"
NUM_SAMPLES = 100  # per gesture

gesture_label = input("🖐️ Enter gesture label (e.g., hello, thanks): ").strip().lower()

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

sample_count = 0
start_saving = False

print(f"\n📸 Collecting {NUM_SAMPLES} samples for: '{gesture_label}'")
print("▶️ Press 's' to start saving | Press 'q' to quit\n")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    image = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if start_saving and sample_count < NUM_SAMPLES:
                data = []
                for lm in hand_landmarks.landmark:
                    data.extend([lm.x, lm.y, lm.z])
                data.append(gesture_label)

                os.makedirs("data", exist_ok=True)
                file_exists = os.path.isfile(CSV_FILE)
                with open(CSV_FILE, mode='a', newline='') as f:
                    writer = csv.writer(f)
                    if not file_exists:
                        header = [f"{axis}{i}" for i in range(21) for axis in "xyz"]
                        header.append("label")
                        writer.writerow(header)
                    writer.writerow(data)
                
                sample_count += 1

    cv2.putText(image, f'Samples: {sample_count}/{NUM_SAMPLES}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Collect Gesture Data", image)
    key = cv2.waitKey(10)
    if key == ord('s'):
        start_saving = True
    elif key == ord('q') or sample_count >= NUM_SAMPLES:
        break

cap.release()
cv2.destroyAllWindows()
print(f"\n✅ {sample_count} samples saved for gesture: '{gesture_label}'")

