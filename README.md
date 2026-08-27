# Predicting Turning Patterns and Vehicle Count Using Camera Feeds 🚦🚗

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-yellow" alt="YOLOv8">
  <img src="https://img.shields.io/badge/DeepSORT-Object%20Tracking-green" alt="DeepSORT">
  <img src="https://img.shields.io/badge/Flask-2.2-lightgrey?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite" alt="SQLite">
</p>

A computer vision-based traffic monitoring system that detects, tracks, counts, and analyzes vehicles from camera feeds while identifying their turning patterns as **Left, Right, or Straight**.

---

## 📌 Overview

**Predicting Turning Patterns and Vehicle Count Using Camera Feeds** is a real-time traffic analysis system built using **YOLOv8, DeepSORT, OpenCV, and Flask**.

The system processes live camera feeds or recorded traffic videos to detect and track vehicles, assign unique tracking IDs, determine their movement direction, and store traffic statistics in a SQLite database.

The collected information is presented through a **Flask-based web dashboard**, providing a simple interface for monitoring vehicle counts, turning patterns, and overall traffic conditions.

---

## ✨ Features

* 🚗 **Real-Time Vehicle Detection** using YOLOv8
* 🎯 **Vehicle Tracking** using DeepSORT
* ↩️ **Turning Pattern Detection** — Left, Right, and Straight
* 🔢 **Vehicle Counting** based on tracked objects
* 🚦 **Traffic Status Estimation** — Normal or Heavy Traffic
* 💾 **SQLite Database Storage** for traffic statistics
* 🌐 **Flask Web Dashboard** for displaying results
* 🎥 **Video Processing** using OpenCV
* 📊 **Traffic Data Analysis** using stored vehicle information
* 🆔 **Unique Vehicle Tracking IDs** to prevent duplicate counting

---

## 🧠 How It Works

The system follows a multi-stage computer vision pipeline:

```text
Camera Feed / Video
        │
        ▼
   YOLOv8 Detection
        │
        ▼
    DeepSORT Tracking
        │
        ▼
 Vehicle Movement Tracking
        │
        ▼
Turning Pattern Classification
        │
        ├── Left
        ├── Right
        └── Straight
        │
        ▼
 Vehicle Count & Traffic Analysis
        │
        ▼
   SQLite Database
        │
        ▼
   Flask Web Dashboard
```

### Detection

YOLOv8 identifies vehicles such as cars, motorcycles, buses, and trucks within each video frame.

### Tracking

DeepSORT assigns a unique ID to detected vehicles and maintains their identity across consecutive frames.

### Turning Pattern Classification

The movement of each tracked vehicle is analyzed across frames to determine whether it is:

* **Left Turn**
* **Right Turn**
* **Straight**

### Traffic Analysis

Vehicle counts and movement information are used to estimate the current traffic condition.

---

## 📂 Project Structure

```text
Predicting turning pattern and vehicle count using camera feeds/
│
├── my_virtual_env/                  # Python virtual environment
│
├── static/
│   ├── images/
│   │   ├── yolo_detection.gif       # YOLO detection demonstration
│   │   ├── rec1.gif                 # Traffic detection recording
│   │   ├── rec2.gif                 # Traffic detection recording
│   │   └── demo_thumbnail.jpg       # Demo thumbnail
│   │
│   ├── videos/
│   │   └── intersection2.mp4        # Sample traffic video
│   │
│   └── style.css                    # Dashboard styling
│
├── templates/
│   └── index.html                   # Flask dashboard interface
│
├── app.py                            # Flask web application
├── test.py                           # Detection and tracking pipeline
├── requirements.txt                  # Python dependencies
├── vehicles.db                       # SQLite traffic database
├── coco.txt                          # YOLO class labels
└── yolov8s.pt                        # YOLOv8 model weights
```

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

* Python 3.10
* pip
* Git
* A compatible camera or traffic video
* Sufficient system resources for YOLOv8 inference

---

## 🔧 Installation

### 1. Clone the Repository

```sh
git clone <your-repository-url>
cd "Predicting turning pattern and vehicle count using camera feeds"
```

### 2. Create a Virtual Environment

#### Windows

```sh
python -m venv my_virtual_env
my_virtual_env\Scripts\activate
```

#### macOS / Linux

```sh
python3 -m venv my_virtual_env
source my_virtual_env/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Run Vehicle Detection and Tracking

```sh
python test.py
```

This starts the vehicle detection and tracking pipeline using YOLOv8 and DeepSORT.

### Start the Flask Dashboard

Open another terminal and run:

```sh
python app.py
```

The dashboard will be available at:

```text
http://127.0.0.1:5003/
```

---

## 📊 Traffic Analysis

The system provides information such as:

| Metric            | Description                                |
| ----------------- | ------------------------------------------ |
| 🚗 Vehicle Count  | Total number of detected vehicles          |
| ↩️ Left Turns     | Vehicles classified as turning left        |
| ↪️ Right Turns    | Vehicles classified as turning right       |
| ⬆️ Straight       | Vehicles continuing straight               |
| 🚦 Traffic Status | Normal or Heavy traffic                    |
| 🕒 Timestamp      | Time associated with recorded traffic data |

---

## 🎥 Detection & Tracking

<p align="center">
  <img src="static/images/rec1.gif" width="42%" alt="Vehicle Detection">
  <img src="static/images/rec2.gif" width="42%" alt="Vehicle Tracking">
</p>

The system combines object detection and tracking to follow individual vehicles through the intersection and analyze their movement.

---

## 🛠️ Technologies Used

| Category                | Technology              | Purpose                                       |
| ----------------------- | ----------------------- | --------------------------------------------- |
| 🐍 Programming Language | Python 3.10             | Core application and computer vision logic    |
| 🧠 Object Detection     | YOLOv8                  | Detects vehicles in video frames              |
| 🔄 Object Tracking      | DeepSORT                | Maintains unique vehicle identities           |
| 🎥 Video Processing     | OpenCV                  | Processes frames and video streams            |
| 🌐 Web Framework        | Flask 2.2               | Provides the traffic monitoring dashboard     |
| 🗃️ Database            | SQLite                  | Stores vehicle and traffic statistics         |
| 📊 Data Processing      | NumPy / Pandas          | Handles numerical and traffic data processing |
| 🎨 Frontend             | HTML / CSS / JavaScript | Dashboard interface                           |
| 🤖 Model                | `yolov8s.pt`            | Pre-trained YOLOv8 model                      |
| 📋 Labels               | `coco.txt`              | Object detection class labels                 |

---

## 📁 Important Files

### `app.py`

Runs the Flask web application and provides the traffic monitoring dashboard.

### `test.py`

Contains the main vehicle detection, tracking, and movement analysis pipeline.

### `vehicles.db`

SQLite database used to store traffic-related information.

### `yolov8s.pt`

Pre-trained YOLOv8 model used for vehicle detection.

### `coco.txt`

Contains the object classes used by the detection model.

---

## 📈 Example Workflow

```text
        Traffic Camera
              │
              ▼
       Video Frame Input
              │
              ▼
        YOLOv8 Detection
              │
              ▼
        Vehicle Detection
              │
              ▼
        DeepSORT Tracking
              │
              ▼
      Track Vehicle Movement
              │
        ┌─────┼─────┐
        ▼     ▼     ▼
      Left  Right  Straight
        │     │     │
        └─────┼─────┘
              ▼
       Vehicle Statistics
              │
              ▼
        SQLite Database
              │
              ▼
       Flask Web Dashboard
```

---

## 🔮 Future Enhancements

* 🚀 Real-time **vehicle speed estimation**
* 📡 Support for **live CCTV/IP camera streams**
* 🤖 Machine learning-based **traffic prediction**
* 🚦 Automated **traffic signal optimization**
* 📍 Multi-intersection traffic monitoring
* 📊 Advanced traffic analytics and historical reports
* ☁️ Cloud-based traffic monitoring
* 📱 Mobile-friendly traffic monitoring dashboard
* 🧠 Improved turning-pattern classification
* 🚘 Vehicle-type-specific traffic analysis

---

## 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

If you would like to improve the project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test the implementation
5. Submit a pull request

---

## 💬 Feedback

Found a bug or have an idea for improving the system?

Open an issue and describe the problem or proposed enhancement.

---

## 📜 License

This project is intended for educational and research purposes.

Please check the repository for the applicable license and third-party model/software licenses before redistributing the project.
