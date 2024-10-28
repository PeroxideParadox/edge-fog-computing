
### README.md

```markdown
# IoT Fog-Cloud Latency Simulation

This project simulates IoT devices offloading tasks to Fog nodes and Cloud servers, comparing latencies. The results are visualized using an HTML page that reads from a CSV file.

```

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/PeroxideParadox/edge-fog-computing.git
    cd edge-fog-computing
    ```

2. Set up and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the simulation script `main.py` to generate data:
    ```bash
    python main.py
    ```

   This will create a `data/results.csv` file with latency information for each task processed by the Fog nodes and Cloud server.

2. To view the latency comparison, open `visualization.html` using a live server.

## Visualization
To open `visualization.html` with a live server (e.g., in Visual Studio Code):
1. Install the **Live Server** extension for VS Code.
2. Right-click on `visualization.html` in the VS Code file explorer and select **Open with Live Server**.

Alternatively, you can use Python's built-in HTTP server:
```bash
# Start the server in the project directory
python -m http.server
```

Then, open your browser and go to `http://localhost:8000/visualization.html` to view the latency comparison between Fog and Cloud.

