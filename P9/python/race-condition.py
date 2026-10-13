# import threading
# import time

# counter = 0

# def tambah():
#     global counter
#     for _ in range(1000):
#         temp = counter 
#         time.sleep(0)
#         counter = temp + 1

# t1 = threading.Thread(target= tambah)
# t2 = threading.Thread(target=tambah)


# t1.start
# t2.start

# t1.join
# t2.join

# print("Harapan :", 2000)
# print("Hasil   :", counter, "<- salah karena race condition")


# PROCES REBUTANNYA PADA THREADS
import threading
import time

counter = 0

def tambah(nama_thread):
    global counter
    for _ in range(1000):
        print(nama_thread, counter)
        temp = counter 
        time.sleep(0)
        counter = temp + 1

t1 = threading.Thread(target= tambah)
t2 = threading.Thread(target=tambah)


t1.start
t2.start

t1.join
t2.join

print("Harapan :", 2000)
print("Hasil   :", counter, "<- salah karena race condition")