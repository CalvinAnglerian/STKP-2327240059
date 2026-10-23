# Materi 7

import threading
import time

saldo_rekening = {
    "Rekening_A": 1000000,
    "Rekening_B": 500000,
    "Rekening_C": 750000
}

# Membuat lock untuk setiap rekening
lock_a = threading.Lock()
lock_b = threading.Lock()
lock_c = threading.Lock()


def transfer_dana_1():
    """Thread 1: Transfer dari Rekening A ke Rekening B."""

    print("Thread 1: Meminta kunci Rekening A...")
    lock_a.acquire()
    print("Thread 1: Berhasil mengunci Rekening A.")

    time.sleep(1)  # Simulasi proses verifikasi

    print("Thread 1: Meminta kunci Rekening B...")
    lock_b.acquire()

    print("Thread 1: Berhasil mengunci Rekening B.")

    # Proses transfer (Critical Section)
    print("Thread 1: Melakukan transfer saldo A ke B...")

    # Melepaskan kunci
    lock_b.release()
    lock_a.release()

    print("Thread 1: Transfer selesai, kunci dilepaskan.")


def transfer_dana_2():
    """Thread 2: Transfer dari Rekening B ke Rekening A."""

    print("Thread 2: Meminta kunci Rekening B...")
    lock_b.acquire()
    print("Thread 2: Berhasil mengunci Rekening B.")

    time.sleep(1)  # Simulasi proses verifikasi

    print("Thread 2: Meminta kunci Rekening A...")
    lock_a.acquire()

    print("Thread 2: Berhasil mengunci Rekening A.")

    # Proses transfer (Critical Section)
    print("Thread 2: Melakukan transfer saldo B ke A...")

    # Melepaskan kunci
    lock_a.release()
    lock_b.release()

    print("Thread 2: Transfer selesai, kunci dilepaskan.")

# Membuat dua thread
t1 = threading.Thread(target=transfer_dana_1)
t2 = threading.Thread(target=transfer_dana_2)

# Menjalankan kedua thread secara bersamaan
t1.start()
t2.start()

# Menunggu kedua thread selesai
t1.join()
t2.join()

print("Semua proses transfer selesai.")

# docker exec -it python python3 app/P10/deadlock.py

# catatan app itu folder python