import csv
import os

#Deklarasi variabel user admin dan password admin
Admin = "Admin122333"
paswordAdmin = "4dm1n00"

def login_admin():
     os.system("cls")
     while True:
        os.system("cls")
        print("-----------------------------------------")
        print("|                                       |")
        print("|         Silahkan Login Admin          |")
        print("|                                       |")
        print("-----------------------------------------")
        masukan_user = input("Masukan User Admin: ")
        masukan_password = input("Masukan Password Admin: ") 

        if masukan_user == "" and masukan_password == "":
            print("Login gagal, silahkan masukan user admin dan password admin!")
        elif masukan_user == Admin and masukan_password == "":
            print("Login gagal, silahkan masukan password!")
        elif masukan_user == "" and masukan_password == paswordAdmin:
            print("Login gagal, silahkan masukan username!")
        elif masukan_user != Admin and masukan_password != paswordAdmin:
            print("Login gagal, silah kan coba lagi!")
        elif masukan_user == Admin and masukan_password != paswordAdmin:
            print("Login gagal password admin salah!")
        elif masukan_user != Admin and masukan_password == paswordAdmin:
            print("Login gagal User Admin salah!")
        elif masukan_user == Admin and masukan_password == paswordAdmin:
            print("Login berhasil!")
            break
        os.system("pause")
login_admin()

