# predict.py

import cv2
import mediapipe as mp
import numpy as np
import joblib

MODEL_PATH = "models/gesture_model.pkl"
model = joblib.load(MODEL_PATH)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

print("🔮 Press 'q' to quit\n")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    image = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    prediction = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            data = []
            for lm in hand_landmarks.landmark:
                data.extend([lm.x, lm.y, lm.z])

            prediction = model.predict([data])[0]

    cv2.putText(image, f'Gesture: {prediction}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Gesture Recognition", image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

