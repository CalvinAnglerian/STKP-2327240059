import socket, sys
with socket.create_connection(("localhost", 3000)) as s:
    s.sendall((sys.argv[1] + "\n").encode())
    print(s.recv(1024).decode().strip())

# catatan replikasi data
# data replikasi 
# docker compose up -d master slave

# docker exec -it master python3 app/p14/master.py # running server master
# docker exec -it slave python3 app/p14/slave.py # running server slave

# # master dapat tulis/baca
# docker exec -it master python3 app/p14/client.py "SET nama Andi"
# docker exec -it master python3 app/p14/client.py "GET nama"

# slave hanya dapat baca saja
# docker exec -it slave python3 app/p14/client.py "GET nama iis"