import pandas as pd
import os
from datetime import datetime

latency_data = []

# Log latency for tasks processed by fog and cloud
def log_latency(device, task_type, created_time, completion_time, location):
    latency = (completion_time - created_time).total_seconds() * 1000  # Latency in ms
    latency_data.append({
        'device': device,
        'task_type': task_type,
        'created_time': created_time,
        'completion_time': completion_time,
        'latency (ms)': latency,
        'location': location
    })

# Save latency data to CSV file
def save_latency_to_csv():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    df = pd.DataFrame(latency_data)
    df.to_csv('data/results.csv', index=False)
    print("Results saved to data/results.csv")
