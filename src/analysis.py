import pandas as pd
import matplotlib.pyplot as plt
import os

# Analyze and plot results for fog and cloud tasks
def analyze_results():
    if not os.path.exists('data/results.csv'):
        print("No results file found.")
        return

    df = pd.read_csv('data/results.csv')
    
    fog_tasks = df[df['location'] == 'Fog']
    cloud_tasks = df[df['location'] == 'Cloud']
    
    plt.figure(figsize=(10, 6))
    plt.plot(fog_tasks['created_time'], fog_tasks['latency (ms)'], label='Fog Latency', color='blue')
    plt.plot(cloud_tasks['created_time'], cloud_tasks['latency (ms)'], label='Cloud Latency', color='red')
    
    plt.xlabel('Task Creation Time')
    plt.ylabel('Latency (ms)')
    plt.title('Fog vs Cloud Latency Comparison')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    analyze_results()
