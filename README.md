# Smart Agriculture System 🌱🤖

An AI-powered agriculture robot designed to detect plant diseases in real time using computer vision and deep learning.  
The system combines **YOLOv8**, **Flask Web Dashboard**, **Arduino Robot Control**, and **Raspberry Pi Deployment** to create a complete smart farming solution.

---
Portfolio Page : team-infinity.netlify.app
---

## 📌 Project Overview

Smart Agriculture System helps farmers monitor crops automatically and detect diseases instantly through a live camera feed.

Once a disease is detected:

✅ The disease name appears on the dashboard  
✅ Confidence score is calculated  
✅ Detection logs are saved automatically  
✅ Robot receives command to move toward target area  
✅ Full monitoring can be accessed remotely through browser

---

## 🚀 Main Features

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

## 🛠 Technologies Used

- Python
- Flask
- YOLOv8 (Ultralytics)
- OpenCV
- Arduino UNO
- L293D Motor Driver
- Raspberry Pi
- HTML / CSS / JavaScript
- CSV Data Logging

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

## 🧠 System Workflow

1. Camera captures live crop images  
2. YOLO model analyzes frames  
3. If disease detected:
   - Dashboard alert shown
   - Detection saved to logs
   - Robot moves automatically
4. If healthy:
   - Robot stops
5. User can monitor system from website

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
``` id="2dwx2r"

---

## ▶ How to Run

### Install Requirements

```bash id="lplczz"
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000

📊 Dashboard Pages
Main Dashboard
Live camera stream
Disease status
Robot ON/OFF buttons
FPS speed monitor

Statistics Page
Detection history
Disease names
Confidence levels
Total records

🎯 Project Goals
Reduce crop loss
Fast disease detection
Smart farm automation
Save time and effort
Low-cost AI solution

🔮 Future Improvements
Auto pesticide spraying
GPS navigation
Mobile App control
Cloud database
Multiple camera support
Solar powered robot
👨‍💻 Team

Infinity Team 🚀
Ahmed Abdullah Ibrahim
Mohamed Hatem Elshahat
Mohamed Reda Abo Ghanam
ElSayed AbdelSattar ElSayed

📌 Final Summary

Smart Agriculture System is a complete intelligent farming solution that integrates Artificial Intelligence + Robotics + IoT to detect plant diseases automatically and assist farmers with real-time monitoring and smart movement control.

This project demonstrates how modern AI technologies can transform traditional agriculture into an efficient, automated, and sustainable smart farming environment.
