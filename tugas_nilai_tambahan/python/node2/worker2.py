
import os
import pandas as pd
from xmlrpc.server import SimpleXMLRPCServer

WORKER_NAME = "worker2"
PORT = 8002

STORAGE_PATH = f"./app/{WORKER_NAME}/range_shard.csv"

server = SimpleXMLRPCServer(
    ("0.0.0.0", PORT),
    allow_none=True
)

print(f"[RPC WORKER {WORKER_NAME}] Berjalan pada port {PORT}...")


def simpan_shard(data_records):
    try:
        if not isinstance(data_records, list):
            return "Error: Data harus berupa list"

        if len(data_records) == 0:
            return "Tidak ada data untuk disimpan"

        df = pd.DataFrame(data_records)

        os.makedirs(os.path.dirname(STORAGE_PATH), exist_ok=True)

        file_exists = os.path.exists(STORAGE_PATH)

        df.to_csv(
            STORAGE_PATH,
            mode="a",
            header=not file_exists,
            index=False
        )

        print(
            f"[{WORKER_NAME}] Berhasil menyimpan "
            f"{len(df)} baris data"
        )

        return f"Sukses: {len(df)} baris tersimpan di {WORKER_NAME}"

    except Exception as e:
        print(f"[{WORKER_NAME}] Error: {str(e)}")
        return f"Error: {str(e)}"


server.register_function(simpan_shard, "simpan_shard")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print(f"\n[{WORKER_NAME}] Server dihentikan.")
    server.server_close()
