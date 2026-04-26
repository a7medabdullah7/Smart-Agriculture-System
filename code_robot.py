from ultralytics import YOLO
import cv2
import serial
import time

# 🔌 الاتصال بالأردوينو
arduino = serial.Serial('COM3', 9600)  # غير COM لو عندك مختلف
time.sleep(2)

# 🧠 الموديل
model = YOLO("dataset/best.pt")

# 📸 الكاميرا
cap = cv2.VideoCapture(0)

print("System Started...")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    # 🔍 تشغيل الموديل
    results = model(frame, imgsz=320, conf=0.2)

    # 🧠 القرار
    if len(results[0].boxes) > 0:
        conf = float(results[0].boxes.conf[0])

        if conf > 0.5:
            print(f"✅ Disease Detected ({conf:.2f})")

            frame = results[0].plot()

            arduino.write(b'1')   # 🔥 هنا المهم
        else:
            print(f"❌ Ignored ({conf:.2f})")
            arduino.write(b'0')
    else:
        print("🟢 Healthy")
        arduino.write(b'0')

    cv2.imshow("YOLO Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()