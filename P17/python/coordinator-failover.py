from xmlrpc.server import SimpleXMLRPCServer
import threading
import time

LAST_SEEN = {}
LOCK = threading.Lock()
TIMEOUT = 6
LEADER = None

def _pick_leader(now: float):
    global LEADER
    alive = [w for w, t in LAST_SEEN.items() if now - t <= TIMEOUT]
    if LEADER not in alive:
        prev = LEADER
        LEADER = alive[0] if alive else None
        if prev != LEADER:
            print(f"[FAILOVER] {prev} -> {LEADER}", flush=True)

def heartbeat(worker_id: str) -> bool:
    now = time.time()
    with LOCK:
        LAST_SEEN[worker_id] = now
        _pick_leader(now)
        return LEADER == worker_id

def checker():
    while True:
        time.sleep(2)
        with LOCK:
            _pick_leader(time.time())

if __name__ == "__main__":
    threading.Thread(target=checker, daemon=True).start()
    srv = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True, logRequests=False)
    srv.register_function(heartbeat, "heartbeat")
    print("[COORDINATOR] :8000", flush=True)
    srv.serve_forever()