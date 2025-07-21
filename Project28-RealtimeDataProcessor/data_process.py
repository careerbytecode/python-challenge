import threading
import time
import random
import queue

data_queue = queue.Queue()

def simulate_data_stream():
    while True:
        sensor_value = round(random.uniform(10.0, 100.0), 2)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        data_queue.put((timestamp, sensor_value))
        time.sleep(1)

def process_data():
    while True:
        if not data_queue.empty():
            timestamp, value = data_queue.get()
            print(f"[{timestamp}] Sensor Reading: {value}°C")
        time.sleep(0.1)

stream_thread = threading.Thread(target=simulate_data_stream, daemon=True)
process_thread = threading.Thread(target=process_data, daemon=True)

stream_thread.start()
process_thread.start()

while True:
    time.sleep(1)

