import simpy
import csv
import random
from datetime import datetime

class IoTDevice:
    def __init__(self, env, device_id, task_id, processing_type, fog_node, cloud_server):
        self.env = env
        self.device_id = device_id
        self.task_id = task_id
        self.processing_type = processing_type
        self.fog_node = fog_node
        self.cloud_server = cloud_server
        self.action = env.process(self.run())

    def run(self):
        created_time = datetime.now()
        
        # Depending on processing type, use fog or cloud for the task
        if self.processing_type == 'Fog':
            yield self.env.process(self.fog_node.process_task(self.device_id, self.task_id, created_time, 'Fog'))
        elif self.processing_type == 'Cloud':
            yield self.env.process(self.cloud_server.process_task(self.device_id, self.task_id, created_time, 'Cloud'))

class FogNode:
    def __init__(self, env, name):
        self.env = env
        self.name = name

    def process_task(self, device_id, task_id, created_time, processing_type):
        # Simulate network latency and processing time
        network_latency = random.uniform(0.1, 0.3)  # Simulate lower latency for fog
        task_complexity = random.uniform(0.5, 2.0)  # Random complexity factor for variability
        total_processing_time = network_latency + task_complexity
        yield self.env.timeout(total_processing_time)
        
        completed_time = datetime.now()
        latency = (completed_time - created_time).total_seconds() * 1000  # Latency in milliseconds
        record_result(device_id, task_id, created_time, completed_time, latency, processing_type)

class CloudServer:
    def __init__(self, env, name):
        self.env = env
        self.name = name

    def process_task(self, device_id, task_id, created_time, processing_type):
        # Simulate network latency and processing time
        network_latency = random.uniform(0.3, 1.0)  # Simulate higher latency for cloud
        task_complexity = random.uniform(1.0, 3.0)  # Random complexity factor for variability
        total_processing_time = network_latency + task_complexity
        yield self.env.timeout(total_processing_time)
        
        completed_time = datetime.now()
        latency = (completed_time - created_time).total_seconds() * 1000  # Latency in milliseconds
        record_result(device_id, task_id, created_time, completed_time, latency, processing_type)

# CSV recording function
def record_result(device_id, task_id, start_time, end_time, latency, processing_type):
    with open('results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f'Device {device_id}', f'Task {task_id}', start_time, end_time, latency, processing_type])

# Simulation setup
env = simpy.Environment()

# Initialize fog node and cloud server
fog_node = FogNode(env, "FogNode")
cloud_server = CloudServer(env, "CloudServer")

# Initialize CSV with headers
with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Device ID", "Task ID", "Start Time", "End Time", "Latency (ms)", "Processing Type"])

# Only two devices per task (one for Fog, one for Cloud)
num_tasks = 3
device_id = 0
for task_id in range(1, num_tasks + 1):
    IoTDevice(env, device_id, task_id, 'Fog', fog_node, cloud_server)
    device_id += 1
    IoTDevice(env, device_id, task_id, 'Cloud', fog_node, cloud_server)
    device_id += 1

# Run simulation
env.run(until=10)
