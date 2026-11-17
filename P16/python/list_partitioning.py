import os
import pandas as pd

input_file = "app/data.csv"
output_dir = "app/output_list"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(input_file)

for kategori, group in df.groupby("kategori"):
    nama_file = f"{output_dir}/partisi_{kategori.lower()}.csv"
    group.to_csv(nama_file, index=False)
    print(f"Berhasil membuat partisi: {nama_file} ({len(group)} baris)")
