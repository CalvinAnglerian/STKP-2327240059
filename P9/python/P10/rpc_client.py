# Materi 8

import xmlrpc.client


proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

no_rek = "12345"

# ltihan
jumlah_setoran = 1000000

print(f"Meminta pengecekan saldo untuk rekening: {no_rek} via RPC...")

# Memanggil fungsi di server seolah-olah fungsi lokal
hasil_saldo = proxy.cek_saldo(no_rek)

# ltihan
# Memanggil fungsi setor tunai di server
hasil_setoran = proxy.setor_tunai(
    no_rek,
    jumlah_setoran
)

print(f"Hasil dari Server - Saldo Anda: Rp {hasil_saldo:,}")
