from tasks import create_environment, simulate
from latency import save_latency_to_csv

if __name__ == "__main__":
    env = create_environment()
    simulate(env)
    save_latency_to_csv()
    print("Simulation complete. Results saved to data/results.csv")
