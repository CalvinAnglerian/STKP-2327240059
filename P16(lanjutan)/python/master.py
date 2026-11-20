import pandas as pd
from xmlrpc.client import ServerProxy

input_file = "./app/data.csv"
df = pd.read_csv(input_file)

workers = {
    "node2": ServerProxy("http://node2:8002/", allow_none=True),
    "node3": ServerProxy("http://node3:8003/", allow_none=True)
}

def route_target(nilai):
    if nilai < 500000:
        return "node2"
    else:
        return "node3"

df["target_worker"] = df["nilai"].apply(route_target)

for worker_name, rpc_proxy in workers.items():
    chunk = df[df["target_worker"] == worker_name].drop(columns=["target_worker"])
    payload = chunk.to_dict(orient="records")
    try:
        print(f"[COORDINATOR] Memanggil fungsi remote ke {worker_name}...")
        response = rpc_proxy.simpan_shard(payload)
        print(f"[COORDINATOR] Respon dari {worker_name}: {response}")
    except Exception as e:
        print(f"[COORDINATOR] Gagal terhubung/RPC ke {worker_name}: {e}")