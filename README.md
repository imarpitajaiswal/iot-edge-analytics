# 🚦 Industrial IoT Edge Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-00FFFF)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C)

---

## 📌 Overview

Industrial IoT Edge Analytics is a real-time computer vision application that detects and counts vehicles from video streams using **YOLOv8 Nano**. The system is designed for edge environments where low latency and minimal hardware requirements are important.

The application provides a lightweight dashboard that performs live inference, displays annotated frames, and reports object counts without requiring cloud-based processing.

---

## ✨ Features

- Real-time vehicle detection
- Live object counting
- Interactive Streamlit dashboard
- YOLOv8 Nano inference
- OpenCV video processing
- CPU-friendly deployment
- Modular project structure
- Easily extendable to CCTV or IP camera feeds

---

## 🏗 Architecture

```
Video Input
      │
      ▼
OpenCV Frame Capture
      │
      ▼
YOLOv8 Nano Inference
      │
      ▼
Vehicle Detection
      │
      ▼
Object Counting
      │
      ▼
Annotated Frames
      │
      ▼
Streamlit Dashboard
```

---

## 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| Computer Vision | OpenCV |
| Object Detection | YOLOv8 Nano |
| Deep Learning | PyTorch |
| Dashboard | Streamlit |

---

## Business Problem

Large logistics hubs and smart city deployments require real-time vehicle monitoring to improve traffic flow, reduce congestion, and optimize fleet operations.

Uploading continuous video streams to the cloud introduces latency, increases bandwidth costs, and may violate data governance policies.

This project demonstrates an edge-first computer vision solution that performs inference locally using YOLOv8.

---

## 📂 Project Structure

```
iot-edge-analytics/
│
├── app.py
├── requirements.txt
├── assets/
│   └── traffic.mp4
├── models/
│   └── yolov8n.pt
├── screenshots/
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/iot-edge-analytics.git

cd iot-edge-analytics

python -m venv .venv

source .venv/bin/activate      # macOS/Linux

# .venv\Scripts\activate       # Windows

pip install -r requirements.txt

streamlit run app.py
```

---

## 🚀 How It Works

1. Capture video frames using OpenCV.
2. Run each frame through the YOLOv8 Nano model.
3. Detect vehicle classes.
4. Draw bounding boxes.
5. Count detected vehicles.
6. Display results in a live Streamlit dashboard.

---

## 📊 Example Output

- Live video visualization
- Vehicle detection boxes
- Running vehicle count
- Detection confidence

---

## 🎯 Applications

- Smart Cities
- Intelligent Transportation Systems
- Warehouse Monitoring
- Parking Analytics
- Industrial Surveillance
- Logistics Monitoring

---

## 🔮 Future Improvements

- Multi-object tracking using ByteTrack
- DeepSORT integration
- MQTT streaming
- Kafka event pipeline
- ONNX optimization
- TensorRT deployment
- Edge deployment on NVIDIA Jetson
- Database logging
- REST API

---

## 📈 Resume Highlights

- Built a real-time computer vision application using YOLOv8 and OpenCV for vehicle detection.
- Designed a Streamlit dashboard for live visualization and analytics.
- Optimized model loading to avoid repeated initialization during inference.
- Structured the application for lightweight CPU-based edge deployment.

---

## 📄 License

MIT License
