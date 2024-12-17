import os
import csv
import random

Saldo = random.randint(1000000, 2500000)

def user_login_and_registration(filename):
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

        # Aktivitas login jika sudah punya akun
        os.system("cls")
        if pilihanku == "1":
            print("|-------------------------|")
            print("|  Silahkan masukan akun  |")
            print("|-------------------------|")
            with open(filename,mode="r") as username:
                reader = csv.DictReader(username)
                data = list(reader)

            masukan_email = input("Masukan Email anda: ")
            masukan_password = input("Masukan Password Anda: ")

            for item in data:
                if masukan_email in item["Email"] and masukan_password in item["Password"]:
                    print("Login berhasil")
                    
                else:
                    print("Anda Gagal Login")
                    break

        elif pilihanku == "2":
            print("|----------------------------|")
            print("|  Silahkan registrasi akun  |")
            print("|----------------------------|")

            email_user = str(input("Masukan Email: "))
            password_user = str(input("Masukan Password: "))

            data_registrasi = [{
                'Email': email_user,
                'Password': password_user,
                'Saldo': Saldo
            }]

            with open(filename,mode="a") as registrasi:
                header = ['Timestamp', 'Username', 'Password', 'Status']
                writer = csv.DictWriter(registrasi, fieldnames= header)
                writer.writerows(data_registrasi)
            
            os.system("pause")






user_login_and_registration("data_akun_pelanggan.csv")