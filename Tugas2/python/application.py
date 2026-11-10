from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

# GANTI IP INI DENGAN IP FISIK PC 3 (DATA TIER / MASTER DB)
DATA_TIER_IP = "192.168.5.237" # Contoh IP PC 3
database = xmlrpc.client.ServerProxy(f"http://{DATA_TIER_IP}:8004/", allow_none=True)

def tampilkan_pesanan():
    print("[APP TIER] Meneruskan request tampilkan pesanan ke Data Tier...", flush=True)
    return database.get_all()

def tambah_pesanan(id_pesanan, menu, jumlah):
    print(f"[APP TIER] Validasi & memproses pesanan: {menu} ({jumlah} pcs)...", flush=True)
    if jumlah <= 0:
        return False
    return database.insert(id_pesanan, menu, jumlah)

server = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
server.register_function(tampilkan_pesanan, "tampilkan_pesanan")
server.register_function(tambah_pesanan, "tambah_pesanan")

print("[APPLICATION TIER] Berjalan di port 8000. Siap menerima request dari PC 1...", flush=True)
server.serve_forever()