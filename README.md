# 📌 Face Authentication Attendance System

## 🔍 Project Overview
The **Face Authentication Attendance System** is a computer vision–based application that uses a live camera feed to **register users, authenticate faces in real time, and automatically mark attendance** with **Punch-IN and Punch-OUT** functionality.

The system is designed to be **reliable, practical, and aligned with real-world biometric attendance systems**, while also demonstrating a clear understanding of **machine learning limitations**.

---

## 🎯 Features
- ✅ Face Registration using live webcam  
- ✅ Real-time Face Recognition  
- ✅ Automatic Punch-IN / Punch-OUT  
- ✅ One IN + One OUT per user per day  
- ✅ Works with real camera input  
- ✅ Handles varying lighting conditions  
- ✅ Basic spoof prevention using motion detection  
- ✅ CSV-based attendance logging  
- ✅ Cooldown mechanism to prevent duplicate entries  

---

## 🧠 Model & Approach Used

### Face Detection & Recognition
- **Library:** `face-recognition` (dlib-based)
- **Approach:** Face Embeddings + Distance Matching

Each detected face is converted into a **128-dimensional embedding**.  
Authentication is performed using **Euclidean distance**, and the **best match** is selected based on the **minimum distance**.

**Recognition Threshold:**
--Distance < 0.6 → Same person
--Distance ≥ 0.6 → Unknown


### Why Face Embeddings?
- No need to train a model from scratch  
- Industry-standard face recognition approach  
- Robust to lighting and pose variations  

---

## 🏗️ System Architecture

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


---

## 🛡️ Spoof Prevention (Basic)

To reduce basic spoofing attempts:
- Frame-to-frame **motion detection** is applied  
- Static images or photos fail to generate motion  

⚠️ This is a **basic attempt** and not enterprise-grade liveness detection.

---

## 🧾 Attendance Logic
- First successful recognition of the day → **IN**
- Second successful recognition of the day → **OUT**
- Further detections on the same day → **Ignored**
- A cooldown period prevents repeated frame-based entries

### Sample `attendance.csv`
--Name,Date,Time,Type
--Aniket,2026-01-28,09:45:12,IN
--Aniket,2026-01-28,17:58:40,OUT


---

## ⚙️ Technologies Used
- **Programming Language:** Python 3.10  
- **Computer Vision:** OpenCV  
- **Face Recognition:** dlib, face-recognition  
- **Data Handling:** pandas  
- **Storage:** CSV  
- **OS Tested On:** Windows  

---

## 📁 Project Structure
face_attendance_system/
│
├── register.py # Face registration
├── recognize.py # Face recognition & attendance
├── spoof.py # Spoof prevention logic
├── attendance.csv # Attendance records (auto-created)
├── faces/
│ └── registered/ # Stored face embeddings (local only)
└── requirements.txt


---

## ▶️ How to Run the Project

### 1️⃣ Activate Virtual Environment
--venv\Scripts\activate
###2️⃣ Register a User (Run Once per User)
--python register.py
###3️⃣ Start Attendance System
--python recognize.py


--Press Q to exit the camera.

###⚠️ Known Limitations

--Not suitable for identical twins

--Performance degrades in very low lighting

--Basic spoof prevention (not production-grade)

--Requires clear frontal face for best results

--Dependent on webcam quality



###🚀 Future Improvements

--Advanced liveness detection (blink / head movement)

--Web dashboard for attendance analytics

--Working hours calculation

--Database integration

--Cloud sync via edge device

###👨‍💻 Author

Aniket Verma
AI / Machine Learning 


###🏁 Conclusion

--This project demonstrates a practical application of computer vision and machine learning, focusing on robust system design rather than theoretical perfection.

--It reflects real-world constraints, ethical considerations, and engineering trade-offs expected at the internship level.
