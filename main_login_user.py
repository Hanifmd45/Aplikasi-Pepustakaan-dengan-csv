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

            






user_login_and_registration("data_pelanggan.csv")