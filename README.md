Smart Agriculture System 🌱🤖

An AI-powered agriculture robot designed to detect plant diseases in real time using computer vision and deep learning. The system combines YOLOv8, Flask Web Dashboard, Arduino Robot Control, and Raspberry Pi Deployment to create a complete smart farming solution.

🌐 Portfolio Page

🚀 Open Team Infinity Portfolio

📌 Project Overview

The Smart Agriculture System helps farmers monitor crops automatically and detect plant diseases instantly through a live camera feed.

Once a disease is detected:

✅ Disease name appears on the dashboard
✅ Confidence score is displayed
✅ Detection logs are saved automatically
✅ Robot receives movement command toward infected area
✅ Full monitoring can be accessed remotely through browser

🚀 Main Features
🎥 Live Camera Disease Detection
🧠 YOLOv8 AI Model
🌐 Flask Web Dashboard
🤖 Robot Movement using Arduino
📊 Detection Statistics Page
⚡ Real-time FPS Counter
💾 CSV Logging System
🍓 Raspberry Pi Ready
📱 Remote Access via Laptop / Mobile
🛠 Technologies Used
Python
Flask
YOLOv8 (Ultralytics)
OpenCV
Arduino UNO
L293D Motor Driver
Raspberry Pi
HTML / CSS / JavaScript
CSV Data Logging
⚙ Hardware Components
Raspberry Pi
Arduino UNO
USB Camera
L293D Motor Driver Shield
2 DC Motors
Robot Chassis
Wheels
Battery Pack
Jumper Wires
🧠 System Workflow
Camera captures live crop images
YOLOv8 model analyzes frames
If disease is detected:
Alert appears on dashboard
Detection saved to logs
Robot moves automatically
If plant is healthy:
Robot stops
User monitors system through web dashboard
📂 Project Structure
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
▶ How to Run
Install Requirements
pip install -r requirements.txt
python app.py

Then open:

http://127.0.0.1:5000
📊 Dashboard Pages
Main Dashboard
Live camera stream
Disease detection status
Robot ON/OFF buttons
FPS performance monitor
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
Cloud database integration
Multiple camera support
Solar-powered robot
👨‍💻 Team Infinity 🚀
Ahmed Abdullah Ibrahim
Mohamed Hatem Elshahat
Mohamed Reda Abo Ghanam
ElSayed AbdelSattar ElSayed
📌 Final Summary

The Smart Agriculture System is a complete intelligent farming solution that integrates Artificial Intelligence + Robotics + IoT to detect plant diseases automatically and assist farmers through real-time monitoring and smart movement control.

This project demonstrates how modern AI technologies can transform traditional agriculture into an efficient, automated, and sustainable smart farming environment.
