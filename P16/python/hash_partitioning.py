import os
import pandas as pd

input_file = "app/data.csv"
output_dir = "app/output_hash"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(input_file)

PARTITION_KEY = 'id'
NUM_PARTITIONS = 2

def get_partition_id(val):
    return abs(hash(str(val))) % NUM_PARTITIONS

df['partition_id'] = df[PARTITION_KEY].apply(get_partition_id)

for p_id, group in df.groupby("partition_id"):
    nama_file = f"{output_dir}/partisi_hash_{p_id}.csv"
    
    group.drop(columns=['partition_id']).to_csv(nama_file, index=False)
    
    print(f"Berhasil membuat partisi: {nama_file} ({len(group)} baris)")