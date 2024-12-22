import csv
import os
import random

Saldo = random.randint(1000000, 2500000)

def registrasi_user(filename):
    while True:
        os.system('cls')
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
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for item in reader:
                if item['Email'] == email_user:                   
                    return print("Username sudah terdaftar!")
                

         
            else:
                with open(filename,mode="a",newline='') as registrasi:
                    header = ['Email','Password','Saldo']
                    writer = csv.DictWriter(registrasi, fieldnames= header)
                    writer.writerows(data_registrasi)
                    print("Anda berhasil mendaftarkan Akun")
                    break

registrasi_user('data_pelanggan.csv')