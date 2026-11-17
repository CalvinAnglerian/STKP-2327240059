import os
import pandas as pd

input_file = "./app/data.csv"

node_shards = {
    "python3": {
        "range_desc": "Nilai < 300.000",
        "path": "./app/node3/range_shard.csv"
    },
    "python2": {
        "range_desc": "Nilai 300.000 - 1.499.999",
        "path": "./app/node2/range_shard.csv"
    },
    "python": {
        "range_desc": "Nilai >= 1.500.000",
        "path": "./app/p16/range_shard.csv"
    }
}

for node_info in node_shards.values():
    os.makedirs(os.path.dirname(node_info["path"]), exist_ok=True)

df = pd.read_csv(input_file)

def route_to_container_node(nilai):
    if nilai < 300000:
        return "python3"
    elif 300000 <= nilai < 1500000:
        return "python2"
    else:
        return "python"

df["target_node"] = df["nilai"].apply(route_to_container_node)

for node_name, node_info in node_shards.items():
    data_shard = df[df["target_node"] == node_name].drop(columns=["target_node"])
    output_path = node_info["path"]
    data_shard.to_csv(output_path, index=False)
    print(f"Shard terkirim ke Container [{node_name}] ({node_info['range_desc']}) -> {len(data_shard)} baris | Path: {output_path}")