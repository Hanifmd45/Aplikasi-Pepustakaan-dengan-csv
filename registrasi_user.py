import csv
import os

def registrasi_user(filename):
    while True:
        os.system('cls')
        print("|----------------------------|")
        print("|  Silahkan registrasi akun  |")
        print("|----------------------------|")

        email_user = str(input("Masukan Email: "))
        password_user = str(input("Masukan Password: "))

        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for item in reader:
                if item['Email'] == email_user:
                    print("Username sudah terdaftar!")
                    return

        # data_registrasi = [{
        #     'Email': email_user,
        #     'Password': password_user
        # }]

        with open(filename,mode="a",newline='') as registrasi:
            header = ['Email','Password']
            writer = csv.DictWriter(registrasi, fieldnames= header)
            if registrasi.tell() == 0:
                writer.writerows([email_user,password_user])
                writer.writerheader()
            os.system('pause')

registrasi_user('data_pelanggan.csv')