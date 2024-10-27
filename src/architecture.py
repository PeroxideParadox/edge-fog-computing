import simpy
import csv
import random
from datetime import datetime

class IoTDevice:
    def __init__(self, env, device_id, task_name, processing_type, fog_node, cloud_server):
        self.env = env
        self.device_id = device_id
        self.task_name = task_name
        self.processing_type = processing_type
        self.fog_node = fog_node
        self.cloud_server = cloud_server
        # Initiate task processing based on type
        self.action = env.process(self.run())

    def run(self):
        created_time = datetime.now()
        
        if self.processing_type == 'Fog':
            yield self.env.process(self.fog_node.process_task(self.device_id, self.task_name, created_time, 'Fog'))
        elif self.processing_type == 'Cloud':
            yield self.env.process(self.cloud_server.process_task(self.device_id, self.task_name, created_time, 'Cloud'))

class FogNode:
    def process_task(self, device_id, task_name, created_time, processing_type):
        # Dynamic network latency for fog
        network_latency = self.network_congestion() * random.uniform(0.1, 0.5)
        
        # Task complexity based on type of task, fog tasks are assumed simpler
        task_complexity = random.uniform(0.5, 1.5) if "Detection" in task_name else random.uniform(0.3, 0.8)
        
        # Calculate total processing time
        total_processing_time = network_latency + task_complexity
        yield self.env.timeout(total_processing_time)
        
        completed_time = datetime.now()
        latency = (completed_time - created_time).total_seconds() * 1000  # Latency in ms
        
        # Record results in CSV
        record_result(device_id, task_name, created_time, completed_time, latency, processing_type)

    def network_congestion(self):
        """Simulates network congestion with a variable factor, higher during 'peak' hours."""
        return random.uniform(0.8, 1.5)  # More variability for dynamic conditions

class CloudServer:
    def process_task(self, device_id, task_name, created_time, processing_type):
        # Dynamic network latency for cloud
        network_latency = self.network_congestion() * random.uniform(0.3, 1.0)
        
        # Task complexity based on type of task, cloud tasks are assumed more complex
        task_complexity = random.uniform(1.0, 3.0) if "Detection" in task_name else random.uniform(0.8, 2.0)
        
        # Calculate total processing time
        total_processing_time = network_latency + task_complexity
        yield self.env.timeout(total_processing_time)
        
        completed_time = datetime.now()
        latency = (completed_time - created_time).total_seconds() * 1000  # Latency in ms
        
        # Record results in CSV
        record_result(device_id, task_name, created_time, completed_time, latency, processing_type)

    def network_congestion(self):
        """Simulates network congestion with a variable factor, indicating high latency during peak hours."""
        return random.uniform(1.0, 1.8)

# CSV recording function
def record_result(device_id, task_name, start_time, end_time, latency, processing_type):
    with open('data/results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f'Device {device_id}', task_name, start_time, end_time, latency, processing_type])

# Initialize CSV with headers
with open('data/results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Device ID", "Task Name", "Start Time", "End Time", "Latency (ms)", "Processing Type"])
