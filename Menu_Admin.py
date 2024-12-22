import os
from tambah_dan_hapus import tambah_buku 
from tambah_dan_hapus import hapus_buku
from main_menu import main_menu

def menu_admin():
    while True:
        print('''
    |-        Welcome to Owl Book       -|
    |                                    |
    |-----0.keluar-----------------------|
    |-----1.Catatan Keuangan-------------|
    |-----2.Menu ACC---------------------|
    |-----3.Tambah Buku------------------|
    |-----4.Hapus Buku-------------------|''')
        
        print("\nMenu Admin")
        print("0.Keluar")
        print("1.Catatan Keuangan")
        print("2.Menu ACC")
        print("3.Tambah Buku")
        print("4.Hapus Buku")
        pilih = input("Pilih Opsi Admin: ")
        
        if pilih == '1':
            print("Catatan Keuangan")
        elif pilih == '2':
            print("Menu ACC")
        elif pilih == '3':
            tambah_buku('data_buku.csv')
        elif pilih == '4':
            hapus_buku('data_buku.csv')
        elif pilih == '0':
            main_menu()
            break
        else:
            print("tolong masukan angka sesuai menu yang ada")
            

menu_admin()
            
            