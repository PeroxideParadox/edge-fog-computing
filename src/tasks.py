from datetime import datetime, timedelta
import random
from latency import log_latency

# Create a sample environment with multiple devices
def create_environment():
    return [f"Device {i}" for i in range(5)]

# Simulate IoT task processing with fog and cloud
def simulate(devices):
    for i in range(20):  # Simulate 20 tasks
        created_time = datetime.now()
        for device in devices:
            task_type = f"Task {i + 1}"
            if random.random() > 0.5:
                process_on_fog(device, task_type, created_time)
            else:
                process_on_cloud(device, task_type, created_time)

# Process task on fog and log latency
def process_on_fog(device, task_type, created_time):
    processing_time = timedelta(milliseconds=random.randint(500, 2000))  # Faster fog processing
    completion_time = created_time + processing_time
    log_latency(device, task_type, created_time, completion_time, "Fog")

# Process task on cloud and log latency
def process_on_cloud(device, task_type, created_time):
    processing_time = timedelta(milliseconds=random.randint(2000, 5000))  # Slower cloud processing
    completion_time = created_time + processing_time
    log_latency(device, task_type, created_time, completion_time, "Cloud")
