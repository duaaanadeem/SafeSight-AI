# 🦺 SafeSight AI

> AI-powered touchless industrial machine control using Computer Vision, Hand Gesture Recognition, and Deep Learning.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📖 Overview

SafeSight AI is a Computer Vision and Deep Learning project designed to improve industrial workplace safety through touchless machine control.

The system recognizes predefined hand gestures in real time using a webcam and translates them into machine commands such as **START**, **SLOW**, and **STOP**. This prototype demonstrates how AI can reduce the need for physical interaction with machinery, especially during emergency situations.

---

## ✨ Features

- 🤖 Real-time hand gesture recognition
- 🎥 Webcam-based gesture detection
- 🧠 Custom TensorFlow/Keras classification model
- ✋ Touchless machine control
- ⚡ Live industrial dashboard
- 🏭 Designed for industrial automation concepts

---

## 🎯 Supported Gestures

| Gesture | Action |
|---------|--------|
| 👍 START | Starts the machine |
| 🟡 SLOW | Reduces machine speed |
| ✋ STOP | Stops the machine immediately |
| ⚪ IDLE | No recognized gesture |

---

## 🏭 Real-World Implementation

In an industrial environment, cameras installed near machinery could detect workers' hand gestures and send the recognized commands to industrial controllers such as:

- PLCs
- Arduino
- Raspberry Pi
- Industrial IoT Controllers

This enables touchless machine operation from a safer distance and can improve response time during emergencies.

---

## 💻 Tech Stack

- Python
- OpenCV
- MediaPipe
- TensorFlow
- Keras
- CVZone
- NumPy

---

## 📂 Project Structure

```
SafeSight-AI
│
├── Model/
│   ├── keras_model.h5
│   └── labels.txt
│
├── data_collection.py
├── main_dashboard.py
├── hand_landmarker.task
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/duaaanadeem/SafeSight-AI.git
```

Navigate into the project

```bash
cd SafeSight-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main_dashboard.py
```

---

## 🎥 Demo

Watch the project demonstration on LinkedIn:

**https://www.linkedin.com/posts/duaa-khan-b3739431a_artificialintelligence-machinelearning-computervision-ugcPost-7476603371299213312-to5i/?**

---

---

## 👩‍💻 Author

**Duaa Nadeem**

If you found this project useful, consider giving it a ⭐ on GitHub!
