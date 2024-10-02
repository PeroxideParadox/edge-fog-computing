import random
from latency import log_latency

# Simulate task creation in the environment
def create_environment():
    devices = [f"Device {i}" for i in range(5)]  # 5 devices generating tasks
    return devices

def simulate(devices):
    current_time = 0
    for i in range(50):  # Simulate 50 tasks
        current_time += 5  # Each task is generated every 5 seconds
        for device in devices:
            # Randomly decide whether to process on Fog or Cloud
            if random.random() > 0.5:  # 50% chance
                process_on_fog(device, current_time)
            else:
                process_on_cloud(device, current_time)

def process_on_fog(device, created_time):
    processing_time = random.randint(1, 3)  # Fog processing takes between 1-3 seconds
    completion_time = created_time + processing_time
    log_latency(f"{device} (Fog)", created_time, completion_time, "Fog")
    print(f"{device} processed on Fog at time {created_time}, completed at {completion_time}")

def process_on_cloud(device, created_time):
    processing_time = random.randint(3, 7)  # Cloud processing takes between 3-7 seconds
    completion_time = created_time + processing_time
    log_latency(f"{device} (Cloud)", created_time, completion_time, "Cloud")
    print(f"{device} processed on Cloud at time {created_time}, completed at {completion_time}")
