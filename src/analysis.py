
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data/results.csv')

# Plot latency comparison
plt.figure(figsize=(10,6))
plt.plot(df['created_time'], df['latency'], label='Latency')
plt.xlabel('Task Created Time')
plt.ylabel('Latency (Time Units)')
plt.title('Task Latency Over Time')
plt.legend()
plt.show()
