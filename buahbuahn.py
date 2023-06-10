from math import comb
n =int(input('Masukan berapa jenis:')) # Jumlah jenis buah dalam keranjang
k =int(input('masukan jumlah yang diambil:'))
jumlah_cara = comb(n + k - 1, k)

print("Jumlah cara yang berbeda:", jumlah_cara)


