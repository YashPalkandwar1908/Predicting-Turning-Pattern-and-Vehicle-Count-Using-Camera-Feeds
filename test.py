import cv2
import numpy as np
from ultralytics import YOLO
import torch
from deep_sort_realtime.deepsort_tracker import DeepSort
import sqlite3

# Check for GPU availability
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load YOLOv8 model
model = YOLO('yolov8s.pt')

# Initialize DeepSORT tracker
deepsort = DeepSort(max_age=30, n_init=3)

# Open video file or webcam
cap = cv2.VideoCapture('./static/videos/cars.mp4')  # Replace with 0 for webcam

# Load class labels (COCO dataset)
with open("coco.txt", "r") as file:
    class_list = file.read().split("\n")

# Variables for counting vehicles and turning patterns
prev_coords = {}
turn_threshold = 10
vehicle_count = 0
track_ids = set()
heavy_traffic_threshold = 10
stop_counter = {}

# Connect to SQLite database
conn = sqlite3.connect('vehicles.db', check_same_thread=False)
c = conn.cursor()

# Create necessary tables
c.execute('''CREATE TABLE IF NOT EXISTS vehicle_count (id INTEGER PRIMARY KEY, count INTEGER DEFAULT 0)''')
c.execute('''CREATE TABLE IF NOT EXISTS traffic_status (id INTEGER PRIMARY KEY, status TEXT DEFAULT 'Normal')''')
c.execute('''CREATE TABLE IF NOT EXISTS current_vehicles (track_id INTEGER PRIMARY KEY, turning_pattern TEXT)''')

c.execute("INSERT OR IGNORE INTO vehicle_count (id, count) VALUES (1, 0)")
c.execute("INSERT OR IGNORE INTO traffic_status (id, status) VALUES (1, 'Normal')")
conn.commit()

# Function to determine turning patterns
def determine_turning_pattern(track_id, prev_pos, curr_pos):
    x1, y1 = prev_pos
    x2, y2 = curr_pos
    delta_x = x2 - x1

    if abs(delta_x) > turn_threshold:
        return "Right Turn" if delta_x > 0 else "Left Turn"
    return "Going Straight"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 360))

    # YOLOv8 object detection
    results = model.predict(frame, verbose=False)
    detections = []

    for box in results[0].boxes:
        if box.conf > 0.5:
            class_id = int(box.cls)
            if class_id >= len(class_list):
                continue
            class_name = class_list[class_id]
            if class_name in ['car', 'truck', 'bus', 'motorbike', 'motorcycle']:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                detections.append(([x1, y1, x2 - x1, y2 - y1], box.conf.cpu().item(), class_id))

    # Clear previous vehicle data
    c.execute("DELETE FROM current_vehicles")
    conn.commit()

    # Update tracker with detections
    tracks = deepsort.update_tracks(detections, frame=frame)
    current_vehicle_count = 0

    for track in tracks:
        if not track.is_confirmed() or track.time_since_update > 1:
            continue

        track_id = track.track_id
        bbox = track.to_tlbr()

        # Assign a new ID if it's a new vehicle
        if track_id not in track_ids:
            track_ids.add(track_id)
            vehicle_count += 1
            c.execute("UPDATE vehicle_count SET count = ?", (vehicle_count,))
            conn.commit()

        curr_center = ((bbox[0] + bbox[2]) // 2, (bbox[1] + bbox[3]) // 2)

        # Determine turning pattern
        if track_id in prev_coords:
            prev_center = prev_coords[track_id]
            turning_pattern = determine_turning_pattern(track_id, prev_center, curr_center)

            c.execute("INSERT OR REPLACE INTO current_vehicles (track_id, turning_pattern) VALUES (?, ?)", (track_id, turning_pattern))
            conn.commit()

            cv2.putText(frame, turning_pattern, (int(bbox[0]), int(bbox[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        prev_coords[track_id] = curr_center

        # Draw bounding box and track ID
        cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {track_id}", (int(bbox[0]), int(bbox[1]) - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        current_vehicle_count += 1

    # Display total vehicle count
    cv2.putText(frame, f"Total Vehicle Count: {vehicle_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Update traffic status
    traffic_status = "Heavy Traffic" if current_vehicle_count > heavy_traffic_threshold else "Normal"
    c.execute("UPDATE traffic_status SET status = ?", (traffic_status,))
    conn.commit()

    # Display traffic status
    cv2.putText(frame, f"Traffic Status: {traffic_status}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("Turning Pattern Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
 
