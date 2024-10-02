import pandas as pd
import os

latency_data = []

def log_latency(task, created_time, completion_time, location):
    latency = completion_time - created_time
    latency_data.append({
        'task': task,
        'created_time': created_time,
        'completion_time': completion_time,
        'latency': latency,
        'location': location
    })

def save_latency_to_csv():
    # Check if the 'data' directory exists, if not, create it
    if not os.path.exists('data'):
        os.makedirs('data')
    
    df = pd.DataFrame(latency_data)
    df.to_csv('data/results.csv', index=False)
    print("Results saved to data/results.csv")
