import os
import pandas as pd
from xmlrpc.server import SimpleXMLRPCServer

import socket
current_hostname = socket.gethostname()

if current_hostname == "node2":
    WORKER_NAME = "node2"
    PORT = 8002
elif current_hostname == "node3":
    WORKER_NAME = "node3"
    PORT = 8003
else:
    WORKER_NAME = "worker_default"
    PORT = 8000

STORAGE_PATH = f"./app/{WORKER_NAME}/range_shard.csv"

server = SimpleXMLRPCServer(("0.0.0.0", PORT), allow_none=True)
print(f"[RPC WORKER {WORKER_NAME}] Berjalan di hostname '{current_hostname}' pada port {PORT}...")

def simpan_shard(data_records):
    try:
        df = pd.DataFrame(data_records)
        os.makedirs(os.path.dirname(STORAGE_PATH), exist_ok=True)
        df.to_csv(STORAGE_PATH, index=False)
        print(f"[RPC WORKER {WORKER_NAME}] Berhasil menyimpan {len(df)} baris data ke {STORAGE_PATH}")
        return f"Sukses tersimpan {len(df)} baris di worker {WORKER_NAME}"
    except Exception as e:
        print(f"[RPC WORKER {WORKER_NAME}] Error saat menyimpan data: {str(e)}")
        return f"Error: {str(e)}"

server.register_function(simpan_shard, "simpan_shard")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print(f"\n[RPC WORKER {WORKER_NAME}] Dihentikan.")