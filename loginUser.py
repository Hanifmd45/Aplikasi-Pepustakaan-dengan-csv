import csv
import os
import detail_buku as db

def user_login(filename):
    while True:
        os.system('cls')
        print("|-------------------------|")
        print("|  Silahkan masukan akun  |")
        print("|  Ketik k untuk kembali  |")
        print("|-------------------------|")
    
        masukan_email = input("Masukan Email anda: ")
        if masukan_email.lower() == "k":
            return
        masukan_password = input("Masukan Password Anda: ")

        with open(filename,mode="r") as username:
            reader = csv.DictReader(username)

            for item in reader:
                if item["Email"] == masukan_email and item["Password"] == masukan_password:
                    print("Login berhasil")        
                    os.system('pause')
                    user = {'Email':item["Email"],
                            'Saldo':item['Saldo']}
                    db.menu_pelanggan(user)
                    return
                    
            else:
                print("Anda Gagal Login")  
                os.system('pause')
# user_login('data_pelanggan.csv')
            