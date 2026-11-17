
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

# IP FISIK PC 3 (DATA TIER / MASTER DB)
DATA_TIER_IP = "192.168.5.23"

database = xmlrpc.client.ServerProxy(
    f"http://{DATA_TIER_IP}:8004/",
    allow_none=True
)

# 1. MENAMPILKAN PESANAN
def tampilkan_pesanan():
    print("[APP TIER] Meneruskan request tampilkan pesanan ke Data Tier...", flush=True)
    return database.get_all()


# 2. MENAMBAH PESANAN
def tambah_pesanan(id_pesanan, menu, jumlah):
    print(f"[APP TIER] Memproses penambahan pesanan: {menu} ({jumlah} pcs)...", flush=True)

    if jumlah <= 0:
        return False

    return database.insert(id_pesanan, menu, jumlah)


# 3. MENGUBAH PESANAN
def ubah_pesanan(id_pesanan, menu, jumlah):
    print(f"[APP TIER] Memproses perubahan pesanan ID {id_pesanan}...", flush=True)

    if jumlah <= 0:
        return False

    return database.update(id_pesanan, menu, jumlah)


# 4. MENGHAPUS PESANAN
def hapus_pesanan(id_pesanan):
    print(f"[APP TIER] Memproses penghapusan pesanan ID {id_pesanan}...", flush=True)

    return database.delete(id_pesanan)


# SERVER APPLICATION TIER
server = SimpleXMLRPCServer(
    ("0.0.0.0", 8000),
    allow_none=True
)

server.register_function(tampilkan_pesanan, "tampilkan_pesanan")
server.register_function(tambah_pesanan, "tambah_pesanan")
server.register_function(ubah_pesanan, "ubah_pesanan")
server.register_function(hapus_pesanan, "hapus_pesanan")

print("[APPLICATION TIER] Berjalan di port 8000. Siap menerima request dari PC 1...", flush=True)

server.serve_forever()
