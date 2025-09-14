# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

DATA_PATH = "data/gesture_data.csv"
MODEL_PATH = "models/gesture_model.pkl"

df = pd.read_csv(DATA_PATH)

X = df.iloc[:, :-1]
y = df.iloc[:, -1].astype(str)  # 🔑 Convert labels to string

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

score = clf.score(X_test, y_test)
print(f"✅ Model trained with accuracy: {score:.2f}")

os.makedirs("models", exist_ok=True)
joblib.dump(clf, MODEL_PATH)
print(f"💾 Model saved to: {MODEL_PATH}")

