import time
import psutil
import requests

SERVER_URL = "http://localhost:3000/api/metrics"

def collect_and_send():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    payload = {
        "node_id": "laptop-nicolas",
        "cpu": cpu,
        "ram": ram
    }

    try:
        response = requests.post(SERVER_URL, json=payload)
        print(f"[+] Sent -> CPU: {cpu}% | RAM: {ram}% | Resp: {response.status_code}")
    except Exception as e:
        print(f"[-] Waiting for Node.js server... ({e})")

if __name__ == "__main__":
    print("Starting Pulse Agent (Press Ctrl+C to exit)...")
    while True:
        collect_and_send()
        time.sleep(3)