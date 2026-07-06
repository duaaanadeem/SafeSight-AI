import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time

# Initialize webcam, hand detector, and gesture classifier
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.8)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# Gesture labels
labels = ["START", "STOP", "SLOW"]
imgSize, offset = 300, 25

# UI color palette (BGR format)
CLR_BG = (28, 28, 28)
CLR_ACCENT = (255, 191, 0)
CLR_TEXT = (240, 240, 240)
CLR_BORDER = (60, 60, 60)

# Initial system state
machine_status, machine_color, speed, step, motion_y = "STANDBY", (120, 120, 120), 0, 0, 0
logs = ["SafeSight AI v2.1 Active"]
last_cmd = ""

while True:
    success, img = cap.read()
    if not success or img is None:
        continue

    img = cv2.resize(img, (640, 480))
    imgOutput = img.copy()

    # Detect a single hand
    hands, img = detector.findHands(img, draw=False)

    # Dashboard sidebar
    cv2.rectangle(imgOutput, (450, 0), (640, 480), CLR_BG, cv2.FILLED)
    cv2.rectangle(imgOutput, (450, 0), (452, 480), CLR_ACCENT, cv2.FILLED)

    cv2.putText(imgOutput, "SAFESIGHT AI", (475, 40),
                cv2.FONT_HERSHEY_TRIPLEX, 0.6, CLR_ACCENT, 1)
    cv2.putText(imgOutput, "INDUSTRIAL MONITOR", (485, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.3, (150, 150, 150), 1)

    if hands:
        hand = hands[0]

        # Draw fingertip landmarks
        for lm in hand['lmList']:
            cv2.circle(imgOutput, (lm[0], lm[1]), 3, CLR_ACCENT, cv2.FILLED)

        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        try:
            # Crop and center the detected hand for classification
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgWhite[:, math.ceil((imgSize - wCal) / 2):
                         math.ceil((imgSize - wCal) / 2) + wCal] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgWhite[math.ceil((imgSize - hCal) / 2):
                         math.ceil((imgSize - hCal) / 2) + hCal, :] = imgResize

            # Predict gesture
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            command = labels[index]

            # Store command history
            if command != last_cmd:
                logs.append(f"{time.strftime('%H:%M')} > {command}")
                if len(logs) > 4:
                    logs.pop(0)
                last_cmd = command

            # Update machine state
            if command == "START":
                machine_status, machine_color, speed, step = "RUNNING", (76, 217, 100), 100, 14
            elif command == "STOP":
                machine_status, machine_color, speed, step = "E-STOP", (88, 86, 214), 0, 0
            elif command == "SLOW":
                machine_status, machine_color, speed, step = "CAUTION", (90, 200, 250), 35, 4

        except:
            pass

    else:
        machine_status, machine_color, speed, step = "IDLE", (100, 100, 100), 0, 0

    # Status indicator
    cv2.circle(imgOutput, (545, 120), 38, CLR_BORDER, 2)
    cv2.circle(imgOutput, (545, 120), 30, machine_color, cv2.FILLED)
    cv2.putText(imgOutput, machine_status, (470, 185),
                cv2.FONT_HERSHEY_DUPLEX, 0.5, CLR_TEXT, 1)

    # Load indicator
    cv2.putText(imgOutput, f"LOAD: {speed}%", (470, 215),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
    cv2.rectangle(imgOutput, (470, 225), (620, 232), CLR_BORDER, cv2.FILLED)
    cv2.rectangle(imgOutput, (470, 225),
                  (470 + int(speed * 1.5), 232), machine_color, cv2.FILLED)

    # Command log
    cv2.rectangle(imgOutput, (465, 260), (625, 340), (40, 40, 40), cv2.FILLED)
    cv2.putText(imgOutput, "TERMINAL_LOG", (470, 275),
                cv2.FONT_HERSHEY_SIMPLEX, 0.3, CLR_ACCENT, 1)

    for i, log in enumerate(reversed(logs)):
        cv2.putText(imgOutput, log, (470, 295 + (i * 12)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, (200, 200, 200), 1)

    # Conveyor animation
    motion_y = (motion_y + step) % 60
    cv2.putText(imgOutput, "VIRTUAL_CONVEYOR", (470, 365),
                cv2.FONT_HERSHEY_SIMPLEX, 0.3, (150, 150, 150), 1)
    cv2.rectangle(imgOutput, (470, 375), (620, 460), (35, 35, 35), cv2.FILLED)

    for i in range(4):
        y_pos = 375 + motion_y + (i * 30)
        if 375 < y_pos < 450:
            cv2.line(imgOutput, (485, y_pos), (605, y_pos), machine_color, 2)

    cv2.imshow("SafeSight AI - Industrial Dashboard", imgOutput)

    # Press 'q' to exit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()