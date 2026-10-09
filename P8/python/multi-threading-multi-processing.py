import time
import os
import multiprocessing
import threading
import psutil

def tugas_thread(nama_proses, nama_thread):
    for i in range(5):
        beban_cpu = sum(x for x in range (50_000_000)) # hanya untuk membebani CPU
        pid = os.getpid() # mendapatkan pid
        tid = threading.get_native_id() # mendapatkan thread id
        core_id = psutil.Process().cpu_num() # mendapatkan core berapa yang sedang bekerja
        waktu_sekarang = time.strftime('%H:%M:%S', time.localtime()) # mendapatkan waktu sekarang
        print(f"[{waktu_sekarang} | {nama_proses} | {nama_thread} | PID: {pid} | TID: {tid} | Core: {core_id}] Loop[ ke-{i} - Selesai menghitung beban!]")
        time.sleep(3)

def tugas_process(nama_proses):
    t1 = threading.Thread(target=tugas_thread, args=(nama_proses, "Thread-1"))
    t2 = threading.Thread(target=tugas_thread, args=(nama_proses, "Thread-2"))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=tugas_process, args=("Proses-A",))
    p2 = multiprocessing.Process(target=tugas_process, args=("Proses-B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()