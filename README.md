📌 Face Authentication Attendance System
🔍 Project Overview

The Face Authentication Attendance System is a computer vision–based application that uses a live camera feed to register users, authenticate faces in real time, and automatically mark attendance with Punch-IN and Punch-OUT functionality.

The system is designed to be reliable, practical, and aligned with real-world biometric attendance systems, while also demonstrating a clear understanding of machine learning limitations.

🎯 Features

✅ Face Registration using live webcam

✅ Real-time Face Recognition

✅ Automatic Punch-IN / Punch-OUT

✅ One IN + One OUT per user per day

✅ Works with real camera input

✅ Handles varying lighting conditions

✅ Basic spoof prevention using motion detection

✅ CSV-based attendance logging

✅ Cooldown mechanism to prevent duplicate entries

🧠 Model & Approach Used
Face Detection & Recognition

Library: face-recognition (dlib-based)

Approach: Face Embeddings + Distance Matching

Each detected face is converted into a 128-dimensional embedding

Authentication is done using Euclidean distance

Best match is selected using minimum distance

Recognition threshold is tuned for live webcam input

Distance < 0.6 → Same person
Distance ≥ 0.6 → Unknown


Why Face Embeddings?

No need to train a model from scratch

Industry-standard approach

Robust to lighting and pose variations.


🏗️ System Architecture:
Webcam Input
     ↓
Face Detection
     ↓
Face Encoding (Embeddings)
     ↓
Best Match Selection
     ↓
Authentication Decision
     ↓
Attendance Logic (IN / OUT)
     ↓
CSV Storage



🛡️ Spoof Prevention (Basic)

To reduce basic spoofing attempts:

Frame-to-frame motion detection is applied

Static images or photos fail to generate motion

This is a basic attempt, not enterprise-grade liveness detection

🧾 Attendance Logic

First successful recognition of the day → IN

Second successful recognition of the day → OUT

Any further detections on the same day → ignored

A cooldown period prevents repeated frame-based entries


Sample attendance.csv
Name,Date,Time,Type
Aniket,2026-01-28,09:45:12,IN
Aniket,2026-01-28,17:58:40,OUT



⚙️ Technologies Used

Programming Language: Python 3.10

Computer Vision: OpenCV

Face Recognition: dlib, face-recognition

Data Handling: pandas

Storage: CSV file

OS Tested On: Windows



📁 Project Structure:
face_attendance_system/
│
├── register.py        # Face registration
├── recognize.py       # Face recognition & attendance
├── spoof.py           # Spoof prevention logic
├── attendance.csv     # Attendance records (auto-created)
├── faces/
│   └── registered/    # Stored face embeddings
└── requirements.txt



▶️ How to Run the Project
1️⃣ Activate virtual environment:
    venv\Scripts\activate

2️⃣ Register a user (run once per user):
    python register.py

3️⃣ Start attendance system:
    python recognize.py
Press Q to exit the camera.




📊 Accuracy Expectations:
Scenario	Expected Performance
Good lighting	95–98% accuracy
Low lighting	85–90% accuracy
Extreme face angles	Reduced accuracy
Photo spoof attempts	Sometimes blocked

⚠️ Known Limitations:

Not suitable for identical twins
Performance degrades in very low lighting
Basic spoof prevention (not production-grade)
Requires clear frontal face for best results
Dependent on webcam quality

🧪 Evaluation Criteria Mapping
Criteria	Implementation
Functional Accuracy	Face embeddings + threshold
System Reliability	Cooldown + strict IN/OUT logic
ML Limitations	Documented clearly
Practical Quality	Real camera, real data logging

🚀 Future Improvements
Advanced liveness detection (blink / head movement)
Web dashboard for attendance analytics
Working hours calculation
Database integration
Cloud deployment with camera gateway

👨‍💻 Author

Aniket Verma
AI / Machine Learning 

🏁 Conclusion

This project demonstrates a practical application of computer vision and machine learning, focusing on robust system design rather than theoretical perfection.
It reflects real-world constraints, ethical considerations, and engineering trade-offs expected at the internship level.