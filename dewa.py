import math
import sys
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
def end():
    print('\n============ Hub Darkoboy and Noid1622 only in github.com =============\n')
    print("\n============= Terima kasih telah menggunakan program ini.===============")
    sys.exit()
def ask_to_continue():
    print('')
    while True:
        user_input = input("\n========>> Apakah Anda ingin melanjutkan (y/n)? ")
        if user_input.lower() == 'y':
            return True
        elif user_input.lower() == 'n':
            print("\nTerima kasih telah menggunakan program ini.")
            sys.exit()
        else:
            print("\nMohon masukkan y atau n saja.")
            
def banyak_kode_dibuat():
    print('''
    Untuk mempermudah proses pengenalan barang yang didisplay pada pameran, maka setiap barang diberi kode khusus. 
    Kode yang diberikan terdiri dari''',GREEN+'2'+RESET,' huruf kapital kemudian diikuti dengan',GREEN+ '5'+RESET, '''angka. Berapa banyak kode yang dapat dibuat?
    hasil ''',BLUE+'67600000'+RESET)
    jumlah_huruf = int(input("Masukkan jumlah huruf kapital: "))
    jumlah_angka = int(input("Masukkan jumlah angka: "))

    jumlah_pilihan = 26 ** jumlah_huruf * 10 ** jumlah_angka
    print("Jumlah kode yang dapat dibuat adalah:", jumlah_pilihan)
    ask_to_continue()

def binomial():
    from math import factorial
    print('Berapakah nilai koefisien dari x^',GREEN+'6'+RESET,' y^',GREEN+'3'+RESET,'dalam hasil ekspansi (x + y)^',RED+'9'+RESET,' menggunakan Teorema Binomial?')
    print('HASIL = \n')
    print('"n" merupakan pangkat ',RED+'ekspansi'+RESET,)
    n = int(input("Masukkan nilai n: "))
    print('"r" mengambil pangkat yang ',GREEN+'terbesar'+RESET)
    r = int(input("Masukkan nilai r: "))

    koefisien = factorial(n) // (factorial(r) * factorial(n - r))
    print("Koefisien binomial C({}, {}) adalah: {}".format(n, r, koefisien))
    lanjut = input('apakah masih ada koefisien(y/n):')
    def ko():    
        print('defautlnya "1"')
        x =int(input('masukkan angka koefisien x: '))
        x1= int(input('masukkan pangkatnya : '))
        y = int(input('masukkan angka koefisien y: '))
        y1 = int(input('masukkan pangkatnya'))
        z = (x**x1)*(y**y1)
        hasil = koefisien*z
        print('hasilnya adalah' ,hasil)
        ask_to_continue()
    if lanjut == 'y':
        ko()
    elif lanjut == 'n':
        return True
        
    
    
def kombinasi():
    from math import comb
    print('Berapa banyak cara untuk memilih empat buah dari sebuah keranjang yang terdiri dari ',GREEN+'4'+RESET,' apel,',GREEN+'4'+RESET,' jeruk dan ',GREEN+'4'+RESET,' mangga?',RED+ '(mangga,jeruk,apel)= 3'+RESET)
    n =int(input('\nMasukan berapa jenis (warna merah): ')) # Jumlah jenis buah dalam keranjang
    k =int(input('masukan jumlah yang diambil: '))
    jumlah_cara = comb(n + k - 1, k)

    print("Jumlah cara yang berbeda:", jumlah_cara)
    ask_to_continue()
    
def deposit():
    print('Seseorang mendepositokan $1000 dalam akun bank dengan yield 8% ',GREEN+'(0.08)'+RESET,' dengan suku bunga majemuk tahunan. Berapakah jumlah total tabungan setelah berjalan ',GREEN+'5'+RESET,' tahun?')
    deposit_awal =int(input('\nmasukan deposit awal($): ')) #1000
    tingkat_bunga =float(input('masukan tingkat bunga(dalam bentuk float): ')) #0.08
    tahun = int(input('masukkan tahun:'))#5

    jumlah_tabungan = deposit_awal * (1 + tingkat_bunga)**tahun
    print(f"Jumlah total tabungan setelah {tahun} tahun: $" + str(round(jumlah_tabungan, 2)))
    ask_to_continue()

def kombinasi_kata():
    from math import factorial
    print('\ncontoh soal :Memanggil fungsi dengan kata ',GREEN+'"MISSISSIPPI"'+RESET,'\n')
    word = input('masukkan kata: ')
    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1

    # Menghitung permutasi dengan pengulangan
    total_permutations = factorial(len(word))
    for count in counts.values():
        total_permutations //= factorial(count)

    print(f"Jumlah cara yang berbeda untuk menyusun huruf-huruf dalam kata {word}: {total_permutations}")
    ask_to_continue()

def jenis_buku():
    from math import comb
    def hitung_jumlah_cara(jenis_buku):
        jumlah_buku = {}
        
        for jenis in jenis_buku:
            jumlah = int(input(f"Masukkan jumlah buku {jenis}: "))
            jumlah_buku[jenis] = jumlah
        
        kombinasi = [comb(jumlah_buku[jenis], 1) for jenis in jenis_buku]
        
        jumlah_cara = 0
        for i in range(len(jenis_buku)):
            for j in range(i+1, len(jenis_buku)):
                jumlah_cara += kombinasi[i] * kombinasi[j]
        
        return jumlah_cara
    print('''Seorang mahasiswa mempunyai sedikit uang dan ia ingin membelanjakan uang tersebut untuk membeli buku kuliah. 
          Di toko buku dia diperhadapkan pada tiga jenis buku, yaitu buku bisnis dengan 6 pilihan, buku komputer dengan 4 pilihan dan buku desain dengan 5 pilihan.
          ''',RED+'Berapa banyak cara jika ia ingin membeli 2 buah buku dari dua jenis buku yang berbeda?\n'+RESET)
    jenis_buku = []
    jumlah_jenis = int(input("Masukkan jumlah jenis buku: "))
    for i in range(jumlah_jenis):
        jenis = input(f"Masukkan jenis buku ke-(nama buku){i+1}: ")
        jenis_buku.append(jenis)

    jumlah_cara = hitung_jumlah_cara(jenis_buku)
    print("Jumlah cara yang berbeda:", jumlah_cara)
    ask_to_continue()
    
def string_bit():
    print('contoh: Berapa banyaknya string bit yang berbeda dengan panjang 9 bit (terdiri dari 0 dan 1)?')
    panjang_bit = int(input("Masukkan panjang bit: "))
    jumlah_string_bit = 2 ** panjang_bit
    print("Jumlah string bit yang berbeda dengan panjang", panjang_bit, "bit adalah:", jumlah_string_bit)
    ask_to_continue()

def rekurensi():
    def rekurensi_min(a1,a0,n,k1,k2):
        if n!=0:
            c=a1
            a2=(k1*a1)-(k2*a0)
            a0=c
            return rekurensi_min(a2,a0,n-1,k1,k2)
        else:
            return (k1*a1)-(k2*a0)

    def rekurensi_plus(a1,a0,n,k1,k2):
        if n!=0:
            c=a1
            a2=(k1*a1)+(k2*a0)
            a0=c
            return rekurensi_plus(a2,a0,n-1,k1,k2)
        else:
            return (k1*a1)+(k2*a0)
        
    def rekurensi_pangkat(a0,n,k1,k2,n_2=0): 
        if n!=0:
            a1=k1*a0+(k2**(n_2))
            n_2+=1
            return rekurensi_pangkat(a1,n-1,k1,k2,n_2)
        else:
            return k1*a0+(k2**(n_2))
    print('''
    1. rekurensi plus (a_n = a_n-1 + 2a_n-2).
    2. rekurensi min (a_n = 6a_n-1  - 9a_n-2).
    3. rekurensi pangkat plus(a_n = 8a_n-1 + 10^n-1)
    4. rekurensi pangkat min(a_n = 8a_n-1 - 10^n-1)
    ''')
    pilih_rekurens=input('Masukan pilihan:')
    if pilih_rekurens=='1':
        a0=int(input('a_0: '))
        a1=int(input('a_1: '))
        n=int(input('a_n (yang di tanya): '))
        k1=int(input('koefisien pertama: '))
        k2=int(input('koefisien kedua: '))
        print(rekurensi_plus(a1,a0,n-2,k1,k2))
    elif pilih_rekurens=='2':
        a0=int(input('a_0: '))
        a1=int(input('a_1: '))   
        n=int(input('a_n (yang di tanya): '))
        k1=int(input('koefisien pertama: '))
        k2=int(input('koefisien kedua: '))
        print(rekurensi_min(a1,a0,n-2,k1,k2))
    elif pilih_rekurens=='3':
        a0=int(input('a_0:'))
        n=int(input('a_n (yang di tanya): '))
        k1=int(input('koefisien pertama: '))
        k2=int(input('koefisien kedua: '))
        print(rekurensi_pangkat(a0,n-1,k1,k2))
    ask_to_continue()
    
def pseudocode():
    m=int(input('M:'))
    k=int(input('K (default masukan 0):'))
    k=0
    for i in range(1,m+1):
        for j in range(i):
            k+=1
    print(f"m={m}, k={k}")
    ask_to_continue()

    
def permutasi():
    from itertools import permutations
    print('Berapa banyak bilangan yang berbeda yang terdiri dari 3 digit yang disusun oleh digit 2,3,4,5,6, dan 7 tanpa ada perulangan simbol?\n')

    digits = []
    num_digits = int(input('masukkan jumlah digit yang ingin dihitung: '))
    jumlah  = int(input('masukkan jumlah angka yang ada disoal:'))
    for i in range(jumlah):
        i = int(input('masukkan angknya: '))
        digits.append(i)

    # Mencari semua permutasi
    permutations = list(permutations(digits, num_digits))

    # Menghitung jumlah permutasi
    count = len(permutations)

    print("Jumlah bilangan yang berbeda:", count)
    ask_to_continue

def strBIT_spesial():
    print("Berapa banyak string delapan bit yang diawali baik dengan 101 ataupun 100?\n")
    panjang_bit=int(input('Masukan panjang bit:'))
    bit_1=input('Masukan range bit pertama:')
    bit_2=input('Masukan range bit kedua:')
    hasil=2**(panjang_bit-len(bit_1))
    hasil=hasil+(2**(panjang_bit-len(bit_2)))
    print(hasil)
    ask_to_continue()

        
        
        


while True:
    print("\n================ Silahkan Pilih Mode ================\n")
    print(" 1. Banyak kode yang dibuat(only huruf)")
    print(" 2. Binomial")
    print(" 3. Kombinasi jenis(buah==buah)")
    print(" 4. Deposit")    
    print(" 5. Kombinasi kata ")
    print(' 6. Jenis buku mahasiswa')
    print(' 7. string bit')
    print(' 8. Rekurensi')
    print(" 9. permutasi")
    print('10. soal bergambar(for)')
    print('11. string bit spesial')
    
    print("\n   ================ Copyright by Darkoboy and Noid1622 ================")
    print("\t================ Follow us on github.com ================\n")
    
    print("\t'TELAH DISEDIAKAN CONTOH SOAL DAN WARNA ",GREEN+'HIJAU'+RESET," MERUPAKAN CONTOH INPUT SERTA WARNA",BLUE+"BIRU"+RESET,"SEBAGAI CONTOH JAWABAN DARI SOAL'\n")

    pilihan=int(input('\nMasukan Pilihan: '))
    if pilihan==1:
        banyak_kode_dibuat()
    elif pilihan==2:
        binomial()
    elif pilihan==3:
        kombinasi()
    elif pilihan == 4:
        deposit()
    elif pilihan == 5:
        kombinasi_kata()
    elif pilihan == 6:
        jenis_buku()
    elif pilihan == 7:
        string_bit()
    elif pilihan == 8:
        rekurensi()
    elif pilihan == 9:
        permutasi()
    elif pilihan == 10:
        pseudocode()
    elif pilihan == 11:
        strBIT_spesial()
    else:
        print('===============masukkan input yang sesuai==============')
        ask_to_continue()
