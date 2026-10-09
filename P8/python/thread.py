import time
import os
import threading
import psutil

def tugas_thread():
    for i in range(5):
        beban_cpu = sum(x for x in range (50_000_000)) # hanya untuk membebani CPU
        pid = os.getpid() # mendapatkan pid
        tid = threading.get_native_id() # mendapatkan thread id
        core_id = psutil.Process().cpu_num() # mendapatkan core berapa yang sedang bekerja
        waktu_sekarang = time.strftime('%H:%M:%S', time.localtime()) # mendapatkan waktu sekarang
        print(f"[{waktu_sekarang} | PID: {pid} | TID: {tid} | Core: {core_id}] Loop[ ke-{i} - Selesai menghitung beban!]")

if __name__ == "__main__":
    tugas_thread()

# Dari luar container
# C:\Users\user602\Documents\GitHub\STKP-2327240059\P8>docker exec -it python python3 app/thread.py
# [02:06:31 | PID: 44 | TID: 44 | Core: 13] Loop[ ke-0 - Selesai menghitung beban!]
# [02:06:33 | PID: 44 | TID: 44 | Core: 13] Loop[ ke-1 - Selesai menghitung beban!]
# [02:06:34 | PID: 44 | TID: 44 | Core: 13] Loop[ ke-2 - Selesai menghitung beban!]
# [02:06:35 | PID: 44 | TID: 44 | Core: 13] Loop[ ke-3 - Selesai menghitung beban!]
# [02:06:36 | PID: 44 | TID: 44 | Core: 13] Loop[ ke-4 - Selesai menghitung beban!]

# What's next:
#     Try Docker Debug for seamless, persistent debugging tools in any container or image → docker debug python
#     Learn more at https://docs.docker.com/go/debug-cli/