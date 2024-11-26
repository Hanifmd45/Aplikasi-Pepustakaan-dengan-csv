def main_menu():
    while True:
        print('''
    |-selamat datang di perpustakaan uty-|
    |                                    |
    |-----0.keluar dari perpustakaan-----|
    |-----1.masuk sebagai admin----------|
    |-----2.masuk sebagai mahasiswa------|''')
        
        pilihan_akun = input("\nmasuk sebagai admin/mahasiswa? :")#Memasukan Pilihan yang ada didaftar

        # Kondisi untuk memproses semua fitur
        if pilihan_akun == "1":
            print("selamat datang admin")
        elif pilihan_akun == "2":
            print("selamat datang mahasiswa")
        elif pilihan_akun == "0":
            print("anda telah keluar dari perpustakaan")    
            break
        else:
            print("tolong masukan angka sesuai menu yang ada")
            
main_menu()