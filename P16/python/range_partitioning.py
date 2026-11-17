import os
import pandas as pd

input_file = "app/data.csv"
output_dir = "app/output_range"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(input_file)

batas_rentang = [0, 300000, 1500000, float("inf")]
label_partisi = ["rendah", "menengah", "tinggi"]

df["kategori_rentang"] = pd.cut(
    df["nilai"], bins=batas_rentang, labels=label_partisi
)

for label, group in df.groupby("kategori_rentang", observed=False):
  hasil_partisi = group.drop(columns=["kategori_rentang"])
  nama_file = f"{output_dir}/range_{label}.csv"
  hasil_partisi.to_csv(nama_file, index=False)
  print(f"Berhasil membuat partisi: {nama_file} ({len(hasil_partisi)} baris)")

# range pasti angka