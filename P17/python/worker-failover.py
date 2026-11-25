import os
import socket
import time
import xmlrpc.client

RPC_URL = os.getenv("RPC_URL", "http://coordinator:8000")
WORKER_ID = os.getenv("WORKER_ID") or socket.gethostname()
INTERVAL = float(os.getenv("INTERVAL", "2"))

if __name__ == "__main__":
    client = xmlrpc.client.ServerProxy(RPC_URL)
    print(f"[WORKER] {WORKER_ID} -> {RPC_URL}", flush=True)
    while True:
        try:
            is_leader = client.heartbeat(WORKER_ID)
            mode = "RUNNING TASK" if is_leader else "STANDBY"
            print(f"[WORKER] {WORKER_ID}: {mode}", flush=True)
        except Exception as err:
            print(f"[WORKER] {WORKER_ID} error: {err}", flush=True)
        time.sleep(INTERVAL)