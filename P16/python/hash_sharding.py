import os
import pandas as pd

input_file = "./app/p16/data.csv"

node_shards = {
    0: {
        "container_name": "python3",
        "path": "./app/node3/hash_shard.csv"
    },
    1: {
        "container_name": "python2",
        "path": "./app/node2/hash_shard.csv"
    },
    2: {
        "container_name": "python",
        "path": "./app/p16/hash_shard.csv"
    }
}

for info in node_shards.values():
    os.makedirs(os.path.dirname(info["path"]), exist_ok=True)

df = pd.read_csv(input_file)

PARTITION_KEY = "nilai"
NUM_PARTITIONS = len(node_shards)

def get_partition_id(val):
    return abs(hash(str(val))) % NUM_PARTITIONS

df["partition_id"] = df[PARTITION_KEY].apply(get_partition_id)

for bucket_id, info in node_shards.items():
    group = df[df["partition_id"] == bucket_id]
    
    output_path = info["path"]
    group.drop(columns=["partition_id"]).to_csv(output_path, index=False)
    
    print(f"Hash Shard (Bucket {bucket_id}) terkirim ke Container [{info['container_name']}] -> {len(group)} baris | Path: {output_path}")