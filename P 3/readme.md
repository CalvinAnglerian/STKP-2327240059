<!-- ERROR -->

Attaching to client-1, server1-1, server2-1, server3-1
server3-1  | Server 3 (Pajak) siap...
server2-1  | Server 2 (Diskon) siap...
server1-1  | Server 1 (Tambah & Forward) siap...


server2-1  | Traceback (most recent call last):
client-1   | Traceback (most recent call last):


server1-1  | Traceback (most recent call last):
client-1   |   File "/app/app.py", line 85, in <module>


server1-1  |   File "/app/app.py", line 22, in <module>


server2-1  |   File "/app/app.py", line 47, in <module>
client-1   |     hasil_tambah, setelah_diskon, pajak, total_akhir = s1.recv(1024).decode().split(',')


client-1   | ValueError: not enough values to unpack (expected 4, got 1)
server1-1  |     pajak, total = s2.recv(1024).decode().split(',')




server1-1  | ValueError: not enough values to unpack (expected 2, got 1)


server1-1 exited with code 1
client-1 exited with code 1
server2-1 exited with code 1
