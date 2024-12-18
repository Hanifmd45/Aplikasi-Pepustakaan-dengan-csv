from loginUser import user_login
from registrasi_user import registrasi_user
import os

def user_login_and_registration():
    while True:
        os.system("cls")
        print("|-------------------------------|")
        print("|                               |")
        print("|Selamat datang di Owl Book Shop|")
        print("|                               |")
        print("|-------------------------------|")
        print("1.Sudah Punya Akun")
        print("2.Belum Punya Akun")

        pilihanku = str(input("Pilih memu: "))

        if pilihanku == "1":
            user_login('data_pelanggan.csv')
        elif pilihanku == "2":
            registrasi_user('data_pelanggan.csv')  
        elif pilihanku == " ":
            print("Harap masukan pilihan anda!")
        else:
            print("Pilihan anda tidak ada di menu")
        os.system('pause')





user_login_and_registration()