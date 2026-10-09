import time
import os
import threading
import psutil

def tugas_thread(nama_thread):
    for i in range(5):
        beban_cpu = sum(x for x in range (50_000_000)) # hanya untuk membebani CPU
        pid = os.getpid() # mendapatkan pid
        tid = threading.get_native_id() # mendapatkan thread id
        core_id = psutil.Process().cpu_num() # mendapatkan core berapa yang sedang bekerja
        waktu_sekarang = time.strftime('%H:%M:%S', time.localtime()) # mendapatkan waktu sekarang
        print(f"[{waktu_sekarang} | PID: {pid} | TID: {tid} | Core: {core_id}] Loop[ ke-{i} - Selesai menghitung beban!]")
        time.sleep(3)

if __name__ == "__main__":
    t1 = threading.Thread(target=tugas_thread, args=("Thread-1",))
    t2 = threading.Thread(target=tugas_thread, args=("Thread-2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()