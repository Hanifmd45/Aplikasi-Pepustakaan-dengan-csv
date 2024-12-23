import csv
import os

def catatan_pemasukan(filename):
    with open('status_pembelian.csv', mode='r') as file:
        reader = list(csv.DictReader(file))

        print("=========================")
        print("--Menu status pemesanan--")
        print("=========================")
        print("")
        urutan = 0
        for data in reader:
            if data['Status'] == "Disetujui":
                urutan += 1
                print(f"{urutan}.{data['Username']} {data['Judul']} Harga: {data['Harga']}")
    
        os.system('pause')

