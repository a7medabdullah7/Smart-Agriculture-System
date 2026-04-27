# Smart Agriculture System 🌱🤖

An AI-powered agriculture robot designed to detect plant diseases in real time using computer vision and deep learning.  
The system combines **YOLOv8**, **Flask Web Dashboard**, **Arduino Robot Control**, and **Raspberry Pi Deployment** to create a complete smart farming solution.

---

## 🌐 Portfolio Page

🚀 **Open Team Infinity Portfolio**  
https://team-infinity-10.netlify.app

---

## 📌 Project Overview

The **Smart Agriculture System** helps farmers monitor crops automatically and detect plant diseases instantly through a live camera feed.

Once a disease is detected:

- ✅ Disease name appears on dashboard  
- ✅ Confidence score is calculated  
- ✅ Detection logs are saved automatically  
- ✅ Robot moves toward target area  
- ✅ Full monitoring available remotely through browser  

---

## 🔥 Features

- 🎥 Live Camera Disease Detection  
- 🧠 YOLOv8 AI Model  
- 🌐 Flask Web Dashboard  
- 🤖 Robot Movement using Arduino  
- 📊 Detection Statistics Page  
- ⚡ Real-time FPS Counter  
- 💾 CSV Logging System  
- 🍓 Raspberry Pi Ready  
- 📱 Remote Access from Laptop / Mobile  

---

## 🧠 Tech Stack

- Python  
- Flask  
- YOLOv8 (Ultralytics)  
- OpenCV  
- Arduino UNO  
- Raspberry Pi  
- HTML / CSS / JavaScript  
- CSV Logging  

---

## ⚙ Hardware Components

- Raspberry Pi  
- Arduino UNO  
- USB Camera  
- L293D Motor Driver Shield  
- 2 DC Motors  
- Robot Chassis  
- Wheels  
- Battery Pack  
- Jumper Wires  

---

## 🔄 System Workflow

1. Camera captures crop images  
2. YOLO model analyzes frames  
3. If disease detected:  
   - Dashboard alert shown  
   - Detection saved to logs  
   - Robot moves automatically  

4. If healthy:  
   - Robot stops  

5. User monitors system from website  

---

## 📂 Project Structure

```bash
Smart-Agriculture-System/
│── app.py
│── requirements.txt
│── best.pt
│── data.csv
│── run.sh
│── templates/
│   ├── index.html
│   └── stats.html
│── robot_code_arduino.ino
