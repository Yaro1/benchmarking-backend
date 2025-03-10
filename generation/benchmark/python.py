import subprocess
import time
import csv
import docker
import os
from queue import Queue
import threading
import json

# Define backends to test
BACKENDS = ["fastapi", "flask", "django", "starlette", "sanic", "tornado", "bottle"]
RESULTS_DIR = "results/python"
os.makedirs(RESULTS_DIR, exist_ok=True)

client = docker.from_env()  # Connect to Docker

def build_and_run_container(backend):
    """Builds and runs a container for the given backend."""
    dockerfile = f"dockerfiles/python/Dockerfile.{backend}"
    image_name = f"benchmark_{backend}"

    print(f"🛠 Building Docker image for {backend}...")
    subprocess.run(["docker", "build", "-t", image_name, "-f", dockerfile, "."], check=True)

    print(f"🚀 Starting container for {backend}...")
    container = client.containers.run(image_name, detach=True, ports={'8000/tcp': 8000})
    time.sleep(5)  # Wait for the backend to start
    return container

def calculate_cpu_percentage(previous_stats, current_stats):
    """Calculates the CPU usage percentage."""
    prev_cpu = previous_stats["cpu_stats"]["cpu_usage"]["total_usage"]
    prev_system = previous_stats["cpu_stats"]["system_cpu_usage"]

    curr_cpu = current_stats["cpu_stats"]["cpu_usage"]["total_usage"]
    curr_system = current_stats["cpu_stats"]["system_cpu_usage"]

    cpu_delta = curr_cpu - prev_cpu
    system_delta = curr_system - prev_system

    num_cpus = len(current_stats["cpu_stats"]["cpu_usage"].get("percpu_usage", [])) or 1

    cpu_percentage = (cpu_delta / system_delta) * num_cpus * 100 if system_delta > 0 else 0

    return cpu_percentage

def get_container_stats(container, duration, queue):
    """Monitors CPU, memory, and network usage of the container."""
    stats = []
    print(f"📡 Monitoring {container.name} for {duration} seconds...")

    start_time = time.time()
    end_time = start_time + duration

    prev_stats = container.stats(stream=False)
    prev_rx = sum(net["rx_bytes"] for net in prev_stats.get("networks", {}).values())

    while time.time() < end_time:
        time.sleep(1)
        usage = container.stats(stream=False)

        cpu_percentage = calculate_cpu_percentage(prev_stats, usage)

        mem_usage = usage["memory_stats"]["usage"]
        mem_limit = usage["memory_stats"]["limit"]
        mem_percentage = (mem_usage / mem_limit) * 100 if mem_limit > 0 else 0

        networks = usage.get("networks", {})
        curr_rx = sum(net["rx_bytes"] for net in networks.values())

        net_throughput = (curr_rx - prev_rx) / (1024 ** 2)  # Convert bytes to MB

        timestamp = time.time()
        stats.append((timestamp, cpu_percentage, mem_percentage, net_throughput))

        prev_stats = usage
        prev_rx = curr_rx

    queue.put(stats)

def run_wrk(backend, url, duration):
    """Runs wrk load test and captures results."""
    cmd = f"wrk -t4 -c100 -d{duration}s -s post.lua {url}"
    print(f"📊 Running load test for {backend} at {url} with POST...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def save_results(backend, wrk_output, resource_stats):
    """Saves benchmark results to a CSV file."""
    csv_file = os.path.join(RESULTS_DIR, f"{backend}_results.csv")
    json_file = os.path.join(RESULTS_DIR, f"{backend}_results.txt")

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "CPU_Usage", "Memory_Usage", "Network_IO"])
        writer.writerows(resource_stats)

    with open(json_file, "w") as f:
        f.write(wrk_output)

    print(f"✅ Results saved: {csv_file}")

def benchmark_backend(backend):
    """Builds, runs, benchmarks, and collects results for a backend in parallel."""
    print(f"\n🚀 Starting benchmark for {backend}...")

    container = build_and_run_container(backend)
    url = f"http://localhost:8000/compute"
    duration = 30  # Benchmark duration in seconds

    queue = Queue()

    # Start stats collection in a thread
    stats_thread = threading.Thread(target=get_container_stats, args=(container, duration, queue))
    stats_thread.start()

    # Run wrk directly in main thread
    wrk_output = run_wrk(backend, url, duration)

    # Wait for stats collection to complete
    stats_thread.join()

    resource_stats = queue.get()

    save_results(backend, wrk_output, resource_stats)

    container.stop()
    container.remove()
    print(f"🛑 Container for {backend} stopped and removed.")

if __name__ == "__main__":
    for backend in BACKENDS:
        benchmark_backend(backend)

    print("\n🎉 All benchmarks completed! Check the results folder.")
