from xmlrpc.server import SimpleXMLRPCServer
import threading


# Data saldo di server pusat
database_rekening = {
    "12345": 5500000,
    "67890": 1250000
}

# Lock untuk melindungi data saldo
saldo_lock = threading.Lock()


# Server multithreading menggunakan threading.Thread
class ThreadedXMLRPCServer(SimpleXMLRPCServer):

    def process_request(self, request, client_address):
        thread = threading.Thread(
            target=self.process_request_thread_manual,
            args=(request, client_address)
        )
        thread.daemon = True
        thread.start()

    def process_request_thread_manual(self, request, client_address):
        try:
            self.finish_request(request, client_address)
        except Exception:
            self.handle_error(request, client_address)
        finally:
            self.shutdown_request(request)


# Fungsi cek saldo
def cek_saldo(nomor_rekening):
    nomor_rekening = str(nomor_rekening)

    with saldo_lock:
        if nomor_rekening not in database_rekening:
            return "Rekening tidak ditemukan"

        return database_rekening[nomor_rekening]


# Fungsi setor tunai
def setor_tunai(nomor_rekening, jumlah):
    nomor_rekening = str(nomor_rekening)

    with saldo_lock:
        if nomor_rekening not in database_rekening:
            return "Rekening tidak ditemukan"

        if jumlah <= 0:
            return "Jumlah setoran harus lebih dari 0"

        database_rekening[nomor_rekening] += jumlah

        return (
            f"Setoran berhasil. Saldo sekarang: "
            f"Rp {database_rekening[nomor_rekening]:,}"
        )


# Fungsi tarik tunai
def tarik_tunai(nomor_rekening, jumlah):
    nomor_rekening = str(nomor_rekening)

    with saldo_lock:
        if nomor_rekening not in database_rekening:
            return "Rekening tidak ditemukan"

        if jumlah <= 0:
            return "Jumlah penarikan harus lebih dari 0"

        if database_rekening[nomor_rekening] < jumlah:
            return "Saldo tidak mencukupi"

        database_rekening[nomor_rekening] -= jumlah

        return (
            f"Penarikan berhasil. Saldo sekarang: "
            f"Rp {database_rekening[nomor_rekening]:,}"
        )


# Membuat server pusat
server = ThreadedXMLRPCServer(
    ("0.0.0.0", 8000),
    allow_none=True
)

# Mendaftarkan fungsi agar bisa dipanggil oleh client
server.register_function(cek_saldo, "cek_saldo")
server.register_function(setor_tunai, "setor_tunai")
server.register_function(tarik_tunai, "tarik_tunai")

print("Server Bank Nusantara Digital berjalan di port 8000...")
print("Server siap menerima banyak permintaan.")

server.serve_forever()
