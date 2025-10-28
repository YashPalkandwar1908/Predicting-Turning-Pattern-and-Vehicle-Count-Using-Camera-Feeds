# **Predicting Turning Patterns and Vehicle Count Using Camera Feeds** 🚦🚗
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python">
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-yellow" alt="YOLOv8">
  <img src="https://img.shields.io/badge/Flask-2.2-lightgrey" alt="Flask">
  <img src="https://img.shields.io/badge/SQL-Database-blue" alt="SQL">
</p>


## **📌 Overview**

This project utilizes **YOLOv8 (Ultralytics) and DeepSORT** to detect and track vehicles from **live camera feeds or recorded videos**. It predicts **vehicle turning patterns (Left, Right, Straight)** and provides **real-time traffic insights** through a web dashboard built with **Flask**.

<!-- 
---

## **🎥 Demo Video**
<p align="center">
    <a href="https://www.youtube.com/watch?v=your_video_id">
        <img src="static/images/demo_thumbnail.jpg" alt="Watch the Demo">
    </a>
</p>


---
 -->


## **🎯 Features**

✅ **Real-time Vehicle Detection** using YOLOv8  
✅ **Object Tracking** with DeepSORT  
✅ **Turning Pattern Classification** (Left, Right, Straight)  
✅ **Traffic Status Estimation** (Normal or Heavy Traffic)  
✅ **Data Storage in SQLite Database (`vehicles.db`)**  
✅ **Web Dashboard** to visualize traffic statistics

---

## **📂 Project Structure**

```
Predicting turning pattern and vehicle count using camera feeds/
│
│── my_virtual_env/               # Virtual environment
│
│── static/                       # Contains CSS for UI and media files
│
│   ├── images/                   # Images & GIFs  
│   │   ├── yolo_detection.gif  
│   │   ├── demo_thumbnail.jpg  
│   ├── videos/                   # Sample videos  
│   │   ├── intersection2.mp4  
│   ├── style.css
│
│── templates/                    # HTML templates for Flask  
│   ├── index.html
│
│── app.py                        # Flask backend for the web dashboard
│
│── test.py                       # Runs object detection & tracking
│
│── requirements.txt              # List of dependencies
│
│── vehicles.db                   # SQLite database storing vehicle counts
│
│── coco.txt                      # Class labels for YOLOv8
│
│── yolov8s.pt                    # Pre-trained YOLOv8 model  
```

---

## **🚀 How to Run**

### **1️⃣ Set up a virtual environment:**

```sh
python -m venv my_virtual_env
my_virtual_env\Scripts\activate  # (Windows)
source my_virtual_env/bin/activate  # (Mac/Linux)
```

### **2️⃣ Install dependencies:**

```sh
pip install -r requirements.txt
```

### **3️⃣ Run object detection & tracking:**

```sh
python test.py
```

### **4️⃣ Start the Flask web dashboard:**

```sh
python app.py
```

### **5️⃣ View real-time traffic insights at:**

```
http://127.0.0.1:5003/
```

---

## **📊 Traffic Analysis**

### **Detection & Tracking in Action**

<p align="center">
    <img src="static/images/rec1.gif" width="40%" style="padding:15px;">
    <img src="static/images/rec2.gif" width="40%" style="padding:15px;">
</p>

---

## 🔧 Technologies Used

| **Category**            | **Technology**             | **Purpose**                                                             |
|-------------------------|----------------------------|--------------------------------------------------------------------------|
| 🐍 **Programming Language** | Python 3.10                 | Core language for backend, logic, and video processing                   |
| 🧠 **Object Detection**      | YOLOv8 (Ultralytics)        | Detects vehicles in real-time from camera feeds                          |
| 🔄 **Object Tracking**       | DeepSORT                    | Tracks vehicles across frames to maintain unique IDs                     |
| 🎥 **Video Processing**      | OpenCV (`cv2`)               | Handles frame extraction, drawing boxes, and visual output               |
| 🌐 **Web Framework**         | Flask 2.2                   | Powers the web dashboard to display insights and stats                   |
| 🗃️ **Database**              | SQLite                      | Stores vehicle counts, turning directions, and timestamps                |
| 🧾 **Data Handling**         | NumPy, Pandas               | Optional: for traffic data aggregation and analysis                      |
| 🎨 **Frontend**              | HTML, CSS, JavaScript       | Renders the dashboard UI with statistics and live data                   |
| 📦 **Model File**            | `yolov8s.pt`                | Pre-trained YOLOv8 model weights for detection                           |
| 📋 **Labels File**           | `coco.txt`                  | Contains class names for object detection                                |


---

## **📌 Future Enhancements**

- 🚀 Add **real-time speed estimation** for vehicles
- 📡 Support for **live CCTV feeds**
- 📊 Improve traffic analysis with **machine learning models**

---

## **🌟 Contributions & Feedback**

Feel free to fork, modify, or suggest improvements!  
💬 **Have an idea? Open an issue!**

