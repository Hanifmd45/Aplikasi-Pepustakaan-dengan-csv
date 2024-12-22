import main_login_user as mlu
import os

def main_menu():
    while True:
        os.system('cls')
        print('''
    |------------------------------------|
    |-        Welcome to Owl Book       -|
    |                                    |
    |-----0.keluar-----------------------|
    |-----1.masuk sebagai admin----------|
    |-----2.masuk sebagai Pelanggan------|''')
        
        pilihan_akun = input("\nmasuk sebagai admin/pelanggan? :")#Memasukan Pilihan yang ada didaftar

        # Kondisi untuk memproses semua fitur
        if pilihan_akun == "1":
            print("selamat datang admin")
        elif pilihan_akun == "2":
            mlu.user_login_and_registration()
        elif pilihan_akun == "0":
            print("anda telah keluar dari aplikasi")    
            break
        else:
            print("tolong masukan angka sesuai menu yang ada")
            
# main_menu()