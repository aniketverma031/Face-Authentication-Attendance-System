import cv2
import face_recognition
import pickle
import os
import pandas as pd
import time
from datetime import datetime
from spoof import motion_detected

# ================= CONFIG =================
DATASET_PATH = "faces/registered"
ATTENDANCE_FILE = "attendance.csv"
THRESHOLD = 0.6          # Face match threshold
COOLDOWN_SECONDS = 10    # Prevent repeated writes
# =========================================

last_punch_time = {}

# -------- Load registered faces ----------
known_faces = {}
for file in os.listdir(DATASET_PATH):
    if file.endswith(".pkl"):
        with open(os.path.join(DATASET_PATH, file), "rb") as f:
            known_faces[file.replace(".pkl", "")] = pickle.load(f)

if len(known_faces) == 0:
    print("❌ No registered users found. Run register.py first.")
    exit()

# -------- Start camera ----------
video = cv2.VideoCapture(0)
prev_frame = None

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # -------- Spoof detection (motion-based) ----------
    if prev_frame is not None:
        if not motion_detected(prev_frame, rgb):
            cv2.putText(frame, "Spoof Detected!",
                        (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2)
            cv2.imshow("Attendance", frame)
            prev_frame = rgb.copy()
            if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
                break
            continue

    # -------- Face detection ----------
    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    # Draw bounding boxes
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

    for face_encoding in face_encodings:
        best_match_name = None
        best_distance = 1.0

        # -------- Find best match ----------
        for name, enc_list in known_faces.items():
            distances = face_recognition.face_distance(enc_list, face_encoding)
            min_dist = distances.min()
            if min_dist < best_distance:
                best_distance = min_dist
                best_match_name = name

        # -------- Recognition decision ----------
        if best_distance < THRESHOLD:
            name = best_match_name
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")
            current_time = time.time()

            # -------- Safe CSV handling ----------
            if os.path.exists(ATTENDANCE_FILE) and os.path.getsize(ATTENDANCE_FILE) > 0:
                df = pd.read_csv(ATTENDANCE_FILE)
            else:
                df = pd.DataFrame(columns=["Name", "Date", "Time", "Type"])

            today_records = df[(df["Name"] == name) & (df["Date"] == date)]

            # -------- Decide punch type ----------
            if len(today_records) == 0:
                punch_type = "IN"
            elif len(today_records) == 1 and today_records.iloc[0]["Type"] == "IN":
                punch_type = "OUT"
            else:
                punch_type = None  # Already completed for today

            # -------- Write attendance (cooldown AFTER decision) ----------
            if punch_type is not None:
                if name in last_punch_time:
                    if current_time - last_punch_time[name] < COOLDOWN_SECONDS:
                        pass
                    else:
                        df.loc[len(df)] = [name, date, time_str, punch_type]
                        df.to_csv(ATTENDANCE_FILE, index=False)
                        last_punch_time[name] = current_time
                else:
                    df.loc[len(df)] = [name, date, time_str, punch_type]
                    df.to_csv(ATTENDANCE_FILE, index=False)
                    last_punch_time[name] = current_time

                cv2.putText(frame, f"{name} - {punch_type}",
                            (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, f"{name}",
                            (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)

        else:
            cv2.putText(frame, "Unknown",
                        (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2)

    cv2.imshow("Attendance", frame)
    prev_frame = rgb.copy()

    if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
        break

video.release()
cv2.destroyAllWindows()
