import time
import os
import psutil

for i in range(5):
    beban_cpu = sum(x for x in range (50_000_000)) # hanya untuk membebani CPU
    pid = os.getpid() # mendapatkan pid
    core_id = psutil.Process().cpu_num() # mendapatkan core berapa yang sedang bekerja
    waktu_sekarang = time.strftime('%H:%M:%S', time.localtime()) # mendapatkan waktu sekarang
    print(f"[{waktu_sekarang} | PID: {pid} | Core: {core_id}] Loop[ ke-{i} - Selesai menghitung beban!]")

# dalam container
#1 docker exec -it nama_container bash (cara masuknya)
# C:\Users\user602\Documents\GitHub\STKP-2327240059>docker exec -it python  bash

#2 pip install psutil : library untuk 

# 3
# root@f46cdac803a7:/# ls app
# output
# process.py

# 4
# root@f46cdac803a7:/# python3 app/process.py
# output:
# [01:57:16 | PID: 37 | Core: 10] Loop[ ke-0 - Selesai menghitung beban!]
# [01:57:17 | PID: 37 | Core: 10] Loop[ ke-1 - Selesai menghitung beban!]
# [01:57:18 | PID: 37 | Core: 10] Loop[ ke-2 - Selesai menghitung beban!]
# [01:57:19 | PID: 37 | Core: 10] Loop[ ke-3 - Selesai menghitung beban!]
# [01:57:20 | PID: 37 | Core: 10] Loop[ ke-4 - Selesai menghitung beban!]