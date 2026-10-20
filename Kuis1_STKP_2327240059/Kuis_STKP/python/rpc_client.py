import xmlrpc.client

proxy = xmlrpc.client.ServerProxy(
    "http://localhost:8000/",
    allow_none=True
)

no_rek = "12345"

print("=== BANK NUSANTARA DIGITAL ===")
print(f"Nomor rekening: {no_rek}")

saldo_awal = proxy.cek_saldo(no_rek)
print(f"\nSaldo awal: Rp {saldo_awal:,}")

jumlah_setoran = 1000000
print(f"\nMenyetor: Rp {jumlah_setoran:,}")
print(proxy.setor_tunai(no_rek, jumlah_setoran))

jumlah_penarikan = 500000
print(f"\nMenarik: Rp {jumlah_penarikan:,}")
print(proxy.tarik_tunai(no_rek, jumlah_penarikan))

saldo_akhir = proxy.cek_saldo(no_rek)
print(f"\nSaldo akhir: Rp {saldo_akhir:,}")
