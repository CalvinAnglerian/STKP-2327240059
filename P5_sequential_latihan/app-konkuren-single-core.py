import time
from concurrent.futures import ThreadPoolExecutor

data = [1, 2, 3, 4]


def tugas_a(angka):
    print(f"Tugas A menghitung angka {angka}")
    hasil = angka * angka
    time.sleep(1)
    return hasil


def tugas_b(angka):
    print(f"Tugas B menghitung angka {angka}")
    hasil = angka * angka
    time.sleep(1)
    return hasil


hasil = []

with ThreadPoolExecutor(max_workers=2) as executor:
    for i in range(0, len(data), 2):
        angka_a = data[i]
        angka_b = data[i + 1]

        hasil_a = executor.submit(tugas_a, angka_a)
        hasil_b = executor.submit(tugas_b, angka_b)

        hasil.append(hasil_a.result())
        hasil.append(hasil_b.result())


print()
print("Semua proses selesai")
print("Hasil =", sum(hasil))

# Concurrent single-core
# angka = [1,2,3,4]
# Tugas A menghitung angka 1 (1*1)
# Tugas B menghitung angka 3 (3*3)
# Tugas A menghitung angka 2 (2*2)
# Tugas B menghitung angka 4 (4*4)
# hasil diatas itu tidak dikeluarkan hasilnya, kalo dikeluarkan jadi sequence
# Hasil  = 30