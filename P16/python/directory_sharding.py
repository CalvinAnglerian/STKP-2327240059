import os
import pandas as pd

input_file = "./app/p16/data.csv"

directory_mapping = [
    {
        "shard_id": "shard_01",
        "container_name": "python3",
        "min_val": 0,
        "max_val": 299999,
        "path": "./app/node3/directory_shard.csv"
    },
    {
        "shard_id": "shard_02",
        "container_name": "python2",
        "min_val": 300000,
        "max_val": 1499999,
        "path": "./app/node2/directory_shard.csv"
    },
    {
        "shard_id": "shard_03",
        "container_name": "python",
        "min_val": 1500000,
        "max_val": float("inf"),
        "path": "./app/p16/directory_shard.csv"
    }
]

for entry in directory_mapping:
    os.makedirs(os.path.dirname(entry["path"]), exist_ok=True)

df = pd.read_csv(input_file)

def lookup_route(nilai):
    for entry in directory_mapping:
        if entry["min_val"] <= nilai <= entry["max_val"]:
            return entry["container_name"]
    return "python" 

df["target_node"] = df["nilai"].apply(lookup_route)

for entry in directory_mapping:
    container_name = entry["container_name"]
    output_path = entry["path"]
    
    data_shard = df[df["target_node"] == container_name].drop(columns=["target_node"])
    
    data_shard.to_csv(output_path, index=False)
    
    print(f"Directory Lookup -> Shard [{entry['shard_id']}] ke Container [{container_name}] | {len(data_shard)} baris | Path: {output_path}")