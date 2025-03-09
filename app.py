from flask import Flask, render_template
import sqlite3
import threading
import time

app = Flask(__name__)

vehicle_count = 0
traffic_status = 'Normal'
current_vehicle_count = 0
turning_stats = {"Right Turn": 0, "Left Turn": 0, "Going Straight": 0}

def fetch_vehicle_data():
    global vehicle_count, traffic_status, current_vehicle_count, turning_stats
    while True:
        try:
            conn = sqlite3.connect('vehicles.db')
            c = conn.cursor()

            c.execute("SELECT count FROM vehicle_count WHERE id = 1")
            result = c.fetchone()
            vehicle_count = result[0] if result else 0

            c.execute("SELECT status FROM traffic_status WHERE id = 1")
            result = c.fetchone()
            traffic_status = result[0] if result else 'Normal'

            c.execute("""
                SELECT turning_pattern, COUNT(*) 
                FROM current_vehicles 
                GROUP BY turning_pattern
            """)
            turning_data = c.fetchall()

            turning_stats = {"Right Turn": 0, "Left Turn": 0, "Going Straight": 0}

            for row in turning_data:
                pattern, count = row
                if pattern in turning_stats:
                    turning_stats[pattern] = count

            c.execute("SELECT COUNT(*) FROM current_vehicles")
            result = c.fetchone()
            current_vehicle_count = result[0] if result else 0

            conn.close()
        except Exception as e:
            print(f"Error fetching data: {e}")

        time.sleep(3)

@app.route('/')
def index():
    return render_template(
        'index.html',
        vehicle_count=vehicle_count,
        traffic_status=traffic_status,
        current_vehicle_count=current_vehicle_count,
        turning_stats=turning_stats
    )

if __name__ == '__main__':
    thread = threading.Thread(target=fetch_vehicle_data)
    thread.daemon = True
    thread.start()
    app.run(debug=True, host='0.0.0.0', port=5003)
