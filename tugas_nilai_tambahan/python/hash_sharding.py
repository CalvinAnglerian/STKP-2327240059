
import pandas as pd
from xmlrpc.client import ServerProxy

# Alamat IP ketiga komputer
node_shards = {
    0: {
        "name": "worker1",
        "url": "http://192.168.1.10:8000"
    },
    1: {
        "name": "worker2",
        "url": "http://192.168.1.11:8000"
    },
    2: {
        "name": "worker3",
        "url": "http://192.168.1.12:8000"
    }
}

# Membaca dataset
input_file = "./app/data.csv"

df = pd.read_csv(input_file)

# Konfigurasi Hash-Based Sharding
PARTITION_KEY = "nilai"
NUM_PARTITIONS = len(node_shards)


def get_partition_id(val):
    return abs(hash(str(val))) % NUM_PARTITIONS


# Menghitung hash setiap data
df["partition_id"] = df[PARTITION_KEY].apply(
    get_partition_id
)

# Membagi data berdasarkan bucket
for bucket_id, info in node_shards.items():

    group = df[
        df["partition_id"] == bucket_id
    ]

    # Menghilangkan kolom partition_id
    shard_data = group.drop(
        columns=["partition_id"]
    )

    # Mengubah data menjadi format yang bisa dikirim XML-RPC
    records = shard_data.astype(object).where(
        pd.notna(shard_data), None
    ).to_dict(orient="records")

    try:
        # Menghubungkan ke worker tujuan
        worker = ServerProxy(
            info["url"],
            allow_none=True
        )

        # Mengirim data ke worker
        result = worker.simpan_shard(records)

        print(
            f"Hash Shard (Bucket {bucket_id}) "
            f"terkirim ke [{info['name']}] "
            f"-> {len(group)} baris"
        )

        print(result)

    except Exception as e:
        print(
            f"Gagal mengirim data ke "
            f"[{info['name']}]: {str(e)}"
        )

print("\nProses Hash-Based Sharding selesai.")
