# Materi 8

from xmlrpc.server import SimpleXMLRPCServer


def cek_saldo(nomor_rekening):
    database_rekening = {
        "12345": 5500000,
        "67890": 1250000
    }

    return database_rekening.get(
        str(nomor_rekening),
        "Rekening tidak ditemukan"
    )

# ltihan
def setor_tunai(nomor_rekening, jumlah):
    nomor_rekening = str(nomor_rekening)

    if nomor_rekening not in cek_saldo:
        return "Rekening tidak ditemukan"

    if jumlah <= 0:
        return "Jumlah setoran harus lebih dari 0"

    cek_saldo[nomor_rekening] += jumlah

    return (
        f"Setoran berhasil. Saldo sekarang: "
        f"Rp {cek_saldo[nomor_rekening]:,}"
    )

server = SimpleXMLRPCServer(("localhost", 8000),allow_none=True)

print("Server Bank RPC berjalan di port 8000...")

server.register_function(cek_saldo, "cek_saldo")

# ltihan
server.register_function(setor_tunai, "setor_tunai")

server.serve_forever()
