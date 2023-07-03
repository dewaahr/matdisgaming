akses=["cakjidan", "raulgonjales","karimbenjema","dewa"]
print("="*46)
print("="*15,"REAL MAGRIB FC","="*15)
print("="*46)
masuk=input(str("Masukan username anda:"))
user=masuk.lower()
player=[]
print("="*5,"Selamat datang",user,"="*5)
while True:
    if user in akses:
        #print("="*5,"Selamat datang",user,"="*5)
        print("1. Tambah data pemain")
        print("2. Hapus data pemain")
        print("3. Tampilkan data pemain")
        print("4. Exit")
        pilihanuser=input("Masukan Pilihan Anda :")
        if pilihanuser=="1":
            tambah=input("Tambahkan Data Pemain :")
            playerbaru=tambah.lower()
            player.append(playerbaru)
            print("Data","'",playerbaru,"'","berhasil ditambahkan")
        elif pilihanuser=="2":
            Playerhapus=input("Masukan Data pemain yang akan dihapus :")
            hapus=Playerhapus.lower()
            if hapus not in player:
                print("Data","'",hapus,"'","tidak ditemukan")
            else:
                player.remove(hapus)
                print("Data","'",hapus,"'","berhasil dihapus")
        elif pilihanuser=="3":
            print("Affiliasi Kerajaan Uttara:")
            print(*player, sep = " | ")
        elif pilihanuser=="4":
            print("Adios....",user,"GLFH")
            break
    else: 
        print("Access Denied")
        break