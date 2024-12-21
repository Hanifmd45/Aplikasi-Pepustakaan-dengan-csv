import csv
from os import system

def list_data_buku():
    with open('data_buku.csv', mode='r') as file:
        reader = list(csv.DictReader(file))
        
        for data in reader:
            print(f"{data['Id']}.{data['Judul']}")


def filter_data_buku():
    with open('data_buku.csv', mode='r') as file:
        reader = list(csv.DictReader(file))
    
    while True:
        system('cls')
        print("|=================|")
        print("|1.Fiksi          |")     
        print("|2.Non-Fiksi      |")
        print("|=================|")      
        input_kategori = input("\nmasukan kategori buku yang ingin dilihat (1/2): ")
        system('cls')

        urutan = 0
        for data in reader:
            if input_kategori == '1':
                # sebuah kondisi untuk mencari semua data yang sesuai dengan kategori fiksi
                if data['Kategori'] == "Fiksi":              
                    urutan += 1
                    print(f"{urutan}.{data['Judul']}") 
            elif input_kategori == "2":
                # sebuah kondisi untuk mencari semua data yang sesuai dengan kategori non-fiksi
                if data['Kategori'] == "Non-fiksi":     
                    urutan += 1
                    print(f"{urutan}.{data['Judul']}") 
        
        # kalo semisal kondisi yang diatas tidak terjalankan berarti variabel urutan akan tetap bernilai 0
        if urutan == 0:
            print("Mohon masukan angka yang sesuai (1/2)")
            system('pause')
        # untuk menghentikan loop bila nilai dari variabel urutan bertambah/lebih dari 0
        else:
            return False
        