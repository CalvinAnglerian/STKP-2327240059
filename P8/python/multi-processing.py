import time
import os
import multiprocessing
import psutil

def tugas_process(nama_proses):
    for i in range(5):
        beban_cpu = sum(x for x in range (50_000_000)) # hanya untuk membebani CPU
        pid = os.getpid() # mendapatkan pid
        core_id = psutil.Process().cpu_num() # mendapatkan core berapa yang sedang bekerja
        waktu_sekarang = time.strftime('%H:%M:%S', time.localtime()) # mendapatkan waktu sekarang
        print(f"[{waktu_sekarang} | PID: {pid} | Core: {core_id}] Loop[ ke-{i} - Selesai menghitung beban!]")
        time.sleep(3)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=tugas_process, args=("Proses-A",))
    p2 = multiprocessing.Process(target=tugas_process, args=("Proses-B",))
    p3 = multiprocessing.Process(target=tugas_process, args=("Proses-C",))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

# dari luar container
# C:\Users\user602\Documents\GitHub\STKP-2327240059\P8>docker exec -it python python3 app/multi-processing.py