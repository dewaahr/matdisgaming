from math import comb

print('3 jenis buku, memilih 2 buku dari 2 jenis berbeda')
jumlah_buku = {}
jenis_buku = ["1", "2", "3"]

for jenis in jenis_buku:
    jumlah = int(input(f"Masukkan jumlah buku {jenis}: "))
    jumlah_buku[jenis] = jumlah

kombinasi = [comb(jumlah_buku[jenis], 1) for jenis in jenis_buku]

jumlah_cara = kombinasi[0] * kombinasi[1] + kombinasi[0] * kombinasi[2] + kombinasi[1] * kombinasi[2]

print("Jumlah cara yang berbeda:", jumlah_cara)
