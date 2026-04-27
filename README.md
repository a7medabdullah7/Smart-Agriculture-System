# Smart Agriculture System 🌱🤖

An AI-powered agriculture robot designed to detect plant diseases in real time using computer vision and deep learning.
The system combines **YOLOv8**, **Flask Web Dashboard**, **Arduino Robot Control**, and **Raspberry Pi Deployment** to create a complete smart farming solution.

---

## 🌐 Portfolio Page

🚀 **Open Team Infinity Portfolio**
[https://team-infinity-10.netlify.app](https://team-infinity-10.netlify.app)

---

## 📌 Project Overview

The **Smart Agriculture System** helps farmers monitor crops automatically and detect plant diseases instantly through a live camera feed.

Once a disease is detected:

* ✅ Disease name appears on dashboard
* ✅ Confidence score is calculated
* ✅ Detection logs are saved automatically
* ✅ Robot moves toward target area
* ✅ Full monitoring available remotely through browser

---

## 🔥 Features

* 🎥 Live Camera Disease Detection
* 🧠 YOLOv8 AI Model
* 🌐 Flask Web Dashboard
* 🤖 Robot Movement using Arduino
* 📊 Detection Statistics Page
* ⚡ Real-time FPS Counter
* 💾 CSV Logging System
* 🍓 Raspberry Pi Ready
* 📱 Remote Access from Laptop / Mobile

---

## 🧠 Tech Stack

* Python
* Flask
* YOLOv8 (Ultralytics)
* OpenCV
* Arduino UNO
* Raspberry Pi
* HTML / CSS / JavaScript
* CSV Logging

---

## ⚙ Hardware Components

* Raspberry Pi
* Arduino UNO
* USB Camera
* L293D Motor Driver Shield
* 2 DC Motors
* Robot Chassis
* Wheels
* Battery Pack
* Jumper Wires

---

## 🔄 System Workflow

1. Camera captures crop images

2. YOLO model analyzes frames

3. If disease detected:

   * Dashboard alert shown
   * Detection saved to logs
   * Robot moves automatically

4. If healthy:

   * Robot stops

5. User monitors system from website

---

## 📂 Project Structure

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

---

## ▶ How to Run

### Install Requirements

pip install -r requirements.txt

### Run Project

python app.py

### Open Browser

[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Dashboard Pages

### Main Dashboard

* Live camera stream
* Disease status
* Robot ON/OFF buttons
* FPS speed monitor

### Statistics Page

* Detection history
* Disease names
* Confidence levels
* Total records

---

## 🎯 Project Goals

* Reduce crop loss
* Fast disease detection
* Smart farm automation
* Save time and effort
* Low-cost AI solution

---

## 🚀 Future Improvements

* Auto pesticide spraying
* GPS navigation
* Mobile App control
* Cloud database
* Multiple camera support
* Solar powered robot

---

## 👨‍💻 Team Infinity

* Ahmed Abdullah Ibrahim
* Mohamed Hatem Elshahat
* Mohamed Reda Abo Ghanam
* ElSayed AbdelSattar ElSayed

---

## 📌 Final Summary

Smart Agriculture System is a complete intelligent farming solution that integrates:

**Artificial Intelligence + Robotics + IoT**

to detect plant diseases automatically and assist farmers with real-time monitoring and smart movement control.

This project demonstrates how modern AI technologies can transform traditional agriculture into an efficient, automated, and sustainable smart farming environment.

---


