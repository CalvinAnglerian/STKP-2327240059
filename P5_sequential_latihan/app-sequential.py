import time

angka = [1, 2, 3, 4, 5, 6, 7, 8]

# Membagi data menjadi 2 tugas
tengah = len(angka) // 2

data_a = angka[:tengah]
data_b = angka[tengah:]

hasil_a = []
hasil_b = []

print("=== PROSES SEQUENTIAL ===")
print()

# Proses Tugas A
for angka in data_a:
    print(f"Tugas A sedang memproses angka {angka}...")
    
    hasil = angka ** 2
    hasil_a.append(hasil)
    
    time.sleep(1)

# Proses Tugas B
for angka in data_b:
    print(f"Tugas B sedang memproses angka {angka}...")
    
    hasil = angka ** 2
    hasil_b.append(hasil)
    
    time.sleep(1)

# Semua proses selesai
print()
print("=== SEMUA PROSES SELESAI ===")
print()

print("Hasil proses:")

for angka, hasil in zip(data_a, hasil_a):
    print(f"Tugas A = {angka}^2 = {hasil}")

for angka, hasil in zip(data_b, hasil_b):
    print(f"Tugas B = {angka}^2 = {hasil}")

print()
print("=== HASIL AKHIR ===")

total_a = sum(hasil_a)
total_b = sum(hasil_b)

print(f"Hasil Tugas A = {total_a}")
print(f"Hasil Tugas B = {total_b}")
print(f"Total = {total_a + total_b}")

# Sequential
# Angka = [1, 2, 3, 4]
# apabila ditambah [1,2,3,4,5,6,7,8] hasilnya langsung muncul saat dilakukan penambahan

# contoh : 
# Tugas A = 1*1 = 1
# Tugas A = 2*2 = 4
# Tugas B = 3*3 = 9
# Tugas B = 4*4 = 16
# Diatas itu tidak perlu di input manual di output
# Hasil = 30