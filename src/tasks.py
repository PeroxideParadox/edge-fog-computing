from datetime import datetime, timedelta
import random
from latency import log_latency

# Generate real-world task names for IoT devices
task_names = [
    "Temperature Analysis", "Humidity Monitoring", "Air Quality Detection", "Motion Detection",
    "Light Intensity Measurement", "Noise Level Detection", "GPS Tracking", "Heart Rate Monitoring",
    "Vehicle Speed Analysis", "Traffic Density Monitoring", "Soil Moisture Measurement",
    "Water Quality Analysis", "Wind Speed Measurement", "Energy Consumption Tracking",
    "Vibration Analysis", "Pressure Monitoring", "Gas Leakage Detection", "Radiation Detection",
    "Fire Detection", "Intruder Alert System"
]

# Create a sample environment with multiple devices
def create_environment():
    return [f"Device {i}" for i in range(5)]

# Simulate IoT task processing with fog and cloud
def simulate(devices):
    task_count = len(task_names)
    for i in range(task_count):  # Use realistic task names
        created_time = datetime.now()
        task_name = task_names[i]
        for device in devices:
            if random.random() > 0.5:
                process_on_fog(device, task_name, created_time)
            else:
                process_on_cloud(device, task_name, created_time)

# Process task on fog and log latency
def process_on_fog(device, task_name, created_time):
    processing_time = timedelta(milliseconds=random.randint(500, 2000))  # Faster fog processing
    completion_time = created_time + processing_time
    log_latency(device, task_name, created_time, completion_time, "Fog")

# Process task on cloud and log latency
def process_on_cloud(device, task_name, created_time):
    processing_time = timedelta(milliseconds=random.randint(2000, 5000))  # Slower cloud processing
    completion_time = created_time + processing_time
    log_latency(device, task_name, created_time, completion_time, "Cloud")
