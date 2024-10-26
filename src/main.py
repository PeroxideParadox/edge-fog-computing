from tasks import create_environment, simulate
from latency import save_latency_to_csv
from analysis import analyze_results

if __name__ == "__main__":
    devices = create_environment()
    simulate(devices)
    save_latency_to_csv()
    analyze_results()
