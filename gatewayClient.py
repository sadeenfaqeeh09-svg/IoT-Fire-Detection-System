import argparse
import json
import socket
from datetime import datetime, timezone

def send(host, port, events):
    with socket.create_connection((host, port)) as sock:
        for e in events:
            payload = json.dumps(e, separators=(",", ":")).encode("utf-8") + b"\n"
            sock.sendall(payload)

def now_utc():
    return datetime.now(timezone.utc).isoformat()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=5000)
    args = p.parse_args()

    events = [
        {"ts": now_utc(), "room": "KITCHEN",  "sensor_id": "CO2_1222177_KITCHEN",    "type": "CO2",   "value": 1200, "status": "ALERT"},
        {"ts": now_utc(), "room": "BEDROOM",  "sensor_id": "SMOKE_1222177_BEDROOM",   "type": "SMOKE", "value": 0.42, "status": "ALERT"},
        {"ts": now_utc(), "room": "KITCHEN",  "sensor_id": "FIRE_1222177_KITCHEN",    "type": "FIRE",  "value": 1,    "status": "ALERT"},
        {"ts": now_utc(), "room": "BEDROOM",  "sensor_id": "CO2_1222177_BEDROOM",     "type": "CO2",   "value": 600,  "status": "OK"},
        {"ts": now_utc(), "room": "DINING",   "sensor_id": "SMOKE_1222177_DINING",    "type": "SMOKE", "value": 0.0,  "status": "OK"},
    ]

    send(args.host, args.port, events)
    print("Sent 5 sample events to cloud server")

if __name__ == "__main__":
    main()
