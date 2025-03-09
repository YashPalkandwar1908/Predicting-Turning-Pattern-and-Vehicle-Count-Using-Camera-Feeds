# **🚦 Predicting Turning Patterns and Vehicle Count Using Camera Feeds**

## **📌 Project Overview**
This project leverages **YOLOv8 (Ultralytics) and DeepSORT** to detect and track vehicles in **live camera feeds or recorded videos**. It predicts **vehicle turning patterns** (Left, Right, Straight) and provides **real-time traffic insights** via a web dashboard built with **Flask**.

---

## **🎯 Features**

- ✅ **Real-time Vehicle Detection** using YOLOv8
- ✅ **Object Tracking** with DeepSORT
- ✅ **Turning Pattern Prediction** (Left, Right, Straight)
- ✅ **Traffic Status Monitoring**
- ✅ **SQLite Database Storage**
- ✅ **Web Dashboard for Visualization**

---

## **📂 Project Structure**

```
Predicting-Turning-Pattern-and-Vehicle-Count/
│── my_virtual_env/         # Virtual environment  
│── static/                 # CSS, images, videos  
│── templates/              # HTML templates  
│── app.py                  # Flask web app  
│── test.py                 # Runs object detection & tracking  
│── requirements.txt        # Dependencies  
│── vehicles.db             # SQLite database  
│── coco.txt                # Class labels for YOLO  
│── yolov8s.pt              # Pre-trained YOLO model  
│── intersection2.mp4       # Sample video  
```

---

## **🚀 Setup & Installation**

### **1️⃣ Create a virtual environment:**
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

### **4️⃣ Start the Flask web app:**
```sh
python app.py
```

### **5️⃣ Access the dashboard at:**
```
http://127.0.0.1:5003/
```

---

## **🔧 Technologies Used**

- **Python**
- **Flask** (Web dashboard)
- **OpenCV** (Video processing)
- **YOLOv8** (Object detection)
- **DeepSORT** (Object tracking)
- **SQLite** (Database storage)

---

## **📌 Future Enhancements**

- 🚀 **Real-time Speed Estimation**
- 📡 **Integration with Live CCTV Feeds**
- 📊 **Advanced Traffic Analytics with AI**

---

## **🌟 Contribute & Feedback**

Feel free to fork, modify, or suggest improvements!\
💬 **Have an idea? Open an issue!**
