import os
import socket
import time
import xmlrpc.client

RPC_URL = os.getenv("RPC_URL", "http://coordinator:8000")
WORKER_ID = os.getenv("WORKER_ID") or socket.gethostname()
INTERVAL = float(os.getenv("INTERVAL", "2"))

if __name__ == "__main__":
    client = xmlrpc.client.ServerProxy(RPC_URL)
    print(f"[WORKER] {WORKER_ID} -> {RPC_URL} every {INTERVAL}s", flush=True)
    while True:
        try:
            ok = client.heartbeat(WORKER_ID)
            print(f"[WORKER] {WORKER_ID} heartbeat={ok}", flush=True)
        except Exception as err:
            print(f"[WORKER] {WORKER_ID} error: {err}", flush=True)
        time.sleep(INTERVAL)

# Push Heartbeat