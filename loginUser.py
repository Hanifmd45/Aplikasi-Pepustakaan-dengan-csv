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

            for item in reader:
                if item["Email"] == masukan_email and item["Password"] == masukan_password:
                    return print("Login berhasil")                    
                    
                elif item["Email"] != masukan_email and item["Password"] != masukan_password:
                    print("Anda Gagal Login")  
                    os.system('pause')
# user_login('data_pelanggan.csv')
            