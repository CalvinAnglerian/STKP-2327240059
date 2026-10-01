# LATIHAN 3 SERVER
import sys
import socket
import time

mode = sys.argv[1]

# SERVER 1
# Tugas:
# 1. Menerima 2 angka dari Client
# 2. Menjumlahkan kedua angka
# 3. Mengirim hasil penjumlahan ke Server 2
# 4. Menerima hasil dari Server 2
# 5. Mengirim hasil akhir kembali ke Client

if mode == 'server1':
    s = socket.socket()
    s.bind(('0.0.0.0', 5001))
    s.listen(1)
    print("Server 1 (Tambah & Forward) siap...")
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024).decode().split(',')
        hasil_tambah = float(data[0]) + float(data[1])
        
        # BARU: Server 1 bertindak sebagai client untuk Server 2 /  # SERVER 1 menghubungi SERVER 2
        s2 = socket.socket()
        s2.connect(('server2', 5002))
        s2.send(str(hasil_tambah).encode())

        # Server 2 mengirim: 
        setelah_diskon, pajak, total_akhir = s2.recv(1024).decode().split(',')
        s2.close()
        
        # Server 1 mengembalikan semua hasil lengkap ke Client asli / # Kirim 4 data ke Client
        conn.send(f"{hasil_tambah},{setelah_diskon},{pajak},{total_akhir}".encode())
        conn.close()

# Latihan
# --- SERVER 2 (Hitung Diskon 5% - BARU + Panggil Server 3 / Pajak) ---
elif mode == 'server2':
    s = socket.socket()
    s.bind(('0.0.0.0', 5002))
    s.listen(1)
    print("Server 2 (Diskon) siap...")
    while True:
        conn, addr = s.accept()
        jumlah = float(conn.recv(1024).decode())    

        # Hitung diskon 5% 
        diskon = jumlah * 0.05
        setelah_diskon = jumlah - diskon
        
        # Server 2 bertindak sebagai client untuk Server 3 (Pajak) / Hubungi Server 3
        # Mengirim data yang sudah didiskon ke Server 3
        s3 = socket.socket()
        s3.connect(('server3', 5003))
        s3.send(str(setelah_diskon).encode())

        # Menerima hasil (pajak dan total_akhir) dari server 3 /  # Server 3 mengirim: pajak, total_akhir
        pajak, total_akhir = s3.recv(1024).decode().split(',')
        s3.close()

        # Kembalikan semua rincian lengkap ke Server 1 / 
        # Kirim ke Server 1
        # setelah_diskon,pajak,total_akhir
        conn.send(f"{setelah_diskon},{pajak},{total_akhir}".encode())
        conn.close()

# --- SERVER 3 (Hitung Pajak 10% - Tetap Sama) ---
elif mode == 'server3':
    s = socket.socket()
    s.bind(('0.0.0.0', 5003))
    s.listen(1)
    print("Server 3 (Pajak) siap...")
    while True:
        conn, addr = s.accept()
        setelah_diskon = float(conn.recv(1024).decode())

        # Hitung pajak 10% dari harga setelah diskon
        pajak = setelah_diskon * 0.10
        total_akhir = setelah_diskon + pajak

        # Kirim kembali hasil pajak dan grand total ke Server 2
        conn.send(f"{pajak},{total_akhir}".encode())
        conn.close()

# CLIENT
elif mode == 'client':
    time.sleep(2)
    angka1, angka2 = "100", "50"

    s1 = socket.socket()
    s1.connect(('server1', 5001))
    s1.send(f"{angka1},{angka2}".encode())
    
    hasil_tambah, setelah_diskon, pajak, total_akhir = s1.recv(1024).decode().split(',')
    s1.close()

    print(
        f"\n=== HASIL DI CLIENT (POLA CHAINING) ==="
        f"\n Angka: {angka1} + {angka2} = {hasil_tambah}"
        f"\n Setelah diskon: {setelah_diskon}"
        f"\n Pajak: {pajak}"
        f"\nTotal: {total_akhir}\n"
    )

# MATERI 2 SERVER
# import sys
# import socket
# import time

# mode = sys.argv[1]

# # --- SERVER 1 (Penjumlahan + Panggil Server 2) ---
# if mode == 'server1':
#     s = socket.socket()
#     s.bind(('0.0.0.0', 5001))
#     s.listen(1)
#     print("Server 1 (Tambah & Forward) siap...")
#     while True:
#         conn, addr = s.accept()
#         data = conn.recv(1024).decode().split(',')
#         hasil_tambah = float(data[0]) + float(data[1])
        
#         # BARU: Server 1 bertindak sebagai client untuk Server 2
#         s2 = socket.socket()
#         s2.connect(('server2', 5002)) #bisa diganti ip lain
#         s2.send(str(hasil_tambah).encode())
#         pajak, total = s2.recv(1024).decode().split(',')
#         s2.close()
        
#         # Server 1 mengembalikan semua hasil lengkap ke Client asli
#         conn.send(f"{hasil_tambah},{pajak},{total}".encode())
#         conn.close()

# # --- SERVER 2 (Hitung Pajak 10% - Tetap Sama) ---
# elif mode == 'server2':
#     s = socket.socket()
#     s.bind(('0.0.0.0', 5002))
#     s.listen(1)
#     print("Server 2 (Pajak) siap...")
#     while True:
#         conn, addr = s.accept()
#         jumlah = float(conn.recv(1024).decode())
#         pajak = jumlah * 0.10
#         total = jumlah + pajak
#         conn.send(f"{pajak},{total}".encode())
#         conn.close()

# elif mode == 'client':
#     time.sleep(2)
#     angka1, angka2 = "100", "50"

#     s1 = socket.socket()
#     s1.connect(('server1', 5001))
#     s1.send(f"{angka1},{angka2}".encode())
    
#     hasil_tambah, pajak, total_akhir = s1.recv(1024).decode().split(',')
#     s1.close()

#     print(f"\n=== HASIL DI CLIENT (POLA CHAINING) ===\nAngka: {angka1} + {angka2} = {hasil_tambah}\nPajak: {pajak}\nTotal: {total_akhir}\n")
