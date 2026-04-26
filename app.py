from flask import Flask, render_template, Response, request
from ultralytics import YOLO
import cv2
import time
import csv
import datetime

# 🔁 تشغيل الأردوينو أو Simulation
USE_ARDUINO = False

if USE_ARDUINO:
    import serial
    try:
        arduino = serial.Serial('COM3', 9600)
        time.sleep(2)
        print("✅ Arduino Connected")
    except:
        arduino = None
        print("❌ Arduino Error")
else:
    arduino = None
    print("⚠️ Running in Simulation Mode")

app = Flask(__name__)

# 🧠 تحميل الموديل
model = YOLO("runs/detect/train58/weights/best.pt")

# 📸 الكاميرا
cap = cv2.VideoCapture(0)

# 🧠 الحالة
current_status = "Starting..."
current_conf = 0

# ⚡ FPS
prev_time = time.time()

# ⏱️ التحكم في التسجيل
last_logged_time = 0
last_logged_disease = ""


# 🔌 إرسال للأردوينو أو Simulation
def send_to_arduino(value):
    if arduino:
        arduino.write(value)
    else:
        print(f"[SIMULATION] Sent: {value}")


# 📝 دالة تسجيل البيانات
def log_detection(disease, conf):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([now, disease, round(conf, 2)])


# 🎥 تشغيل الكاميرا + AI
def generate_frames():
    global current_status, current_conf, prev_time
    global last_logged_time, last_logged_disease

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 🔍 تشغيل الموديل
        results = model(frame, imgsz=320, conf=0.25)

        current_status = "🟢 Healthy"
        current_conf = 0

        if len(results[0].boxes) > 0:
            conf = float(results[0].boxes.conf[0])
            cls_id = int(results[0].boxes.cls[0])
            disease = results[0].names[cls_id]

            if conf > 0.6:
                current_status = f"⚠️ {disease}"
                current_conf = conf

                frame = results[0].plot()

                send_to_arduino(b'1')

                # ✅ التسجيل الذكي
                now_time = time.time()

                if (now_time - last_logged_time > 2) or (disease != last_logged_disease):
                    log_detection(disease, conf)
                    last_logged_time = now_time
                    last_logged_disease = disease

            else:
                current_status = "Low confidence"
                current_conf = conf
                send_to_arduino(b'0')

        else:
            send_to_arduino(b'0')

        # ⚡ FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 📡 تحويل الصورة
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# 🌐 الصفحة الرئيسية
@app.route('/')
def index():
    return render_template("index.html",
                           status=current_status,
                           conf=current_conf)


# 🎥 فيديو لايف
@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# 🎮 التحكم في الروبوت
@app.route('/control', methods=['POST'])
def control():
    action = request.form.get('action')

    if action == "on":
        print("Robot ON")
        send_to_arduino(b'1')

    elif action == "off":
        print("Robot OFF")
        send_to_arduino(b'0')

    return ('', 204)


# 📊 صفحة الإحصائيات
@app.route('/stats')
def stats():
    data = []
    try:
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    except:
        pass

    return render_template('stats.html', data=data)


# 🚀 تشغيل السيرفر
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)