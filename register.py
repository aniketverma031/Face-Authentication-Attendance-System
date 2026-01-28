import cv2
import face_recognition
import os
import pickle

DATASET_PATH = "faces/registered"
os.makedirs(DATASET_PATH, exist_ok=True)

name = input("Enter your name: ").strip()
file_path = os.path.join(DATASET_PATH, f"{name}.pkl")

# Prevent duplicate registration
if os.path.exists(file_path):
    print(f" User '{name}' is already registered.")
    exit()

video = cv2.VideoCapture(0)
encodings = []

print("Capturing face samples. Press Q to stop.")

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for enc in face_encodings:
        encodings.append(enc)

    cv2.imshow("Register Face", frame)

    if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
        break

video.release()
cv2.destroyAllWindows()

if len(encodings) == 0:
    print(" No face detected.")
    exit()

with open(file_path, "wb") as f:
    pickle.dump(encodings, f)

print(f"✅ Face registered successfully for {name}")
