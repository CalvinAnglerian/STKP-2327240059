from xmlrpc.server import SimpleXMLRPCServer
import threading
import time

LAST_SEEN = {}
TIMEOUT = 6

def heartbeat(worker_id: str) -> bool:
    LAST_SEEN[worker_id] = time.time()
    return True

def checker():
    while True:
        time.sleep(2)
        now = time.time()
        for wid, ts in list(LAST_SEEN.items()):
            age = now - ts
            status = "ALIVE" if age <= TIMEOUT else "DEAD"
            print(f"[MONITOR] {wid}: {status} ({age:.1f}s)", flush=True)

if __name__ == "__main__":
    threading.Thread(target=checker, daemon=True).start()
    server = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True, logRequests=False)
    server.register_function(heartbeat, "heartbeat")
    print("[MONITOR] RPC listening on :8000", flush=True)
    server.serve_forever()

# Push Heartbeat