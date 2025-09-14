import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import joblib

# Streamlit page setup
st.set_page_config(page_title="SignScribe", layout="centered")
st.title("🤟 SignScribe: Gesture to Text Translator")

# Load the trained model
model = joblib.load("models/gesture_model.pkl")

# UI Elements
run = st.checkbox('📷 Start Camera')
FRAME_WINDOW = st.image([])
gesture_placeholder = st.empty()  # This keeps a single line updating (not multiple prints)

# Mediapipe hands setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Start camera
cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        st.warning("⚠️ Camera not found.")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    prediction = "..."

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Predict using model
            try:
                data = []
                for lm in hand_landmarks.landmark:
                    data.extend([lm.x, lm.y, lm.z])
                prediction = model.predict([data])[0]
            except Exception as e:
                prediction = "❌ Error: Model prediction failed"

    # Update one single line for prediction
    gesture_placeholder.subheader(f"✍️ Predicted Gesture: `{prediction}`")
    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

cap.release()
