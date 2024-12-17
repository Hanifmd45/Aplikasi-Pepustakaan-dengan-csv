import csv
import os

def user_login(filename):
    while True:
        os.system('cls')
        print("|-------------------------|")
        print("|  Silahkan masukan akun  |")
        print("|-------------------------|")
        masukan_email = input("Masukan Email anda: ")
        masukan_password = input("Masukan Password Anda: ")

        with open(filename,mode="r") as username:
            reader = csv.DictReader(username)
            data = list(reader)

            for item in data:
                if masukan_email in item["Email"] and masukan_password in item["Password"]:
                    print("Login berhasil")
                    
                else:
                    print("Anda Gagal Login")
                    break
                os.system('pause')
user_login('data_pelanggan.csv')
            