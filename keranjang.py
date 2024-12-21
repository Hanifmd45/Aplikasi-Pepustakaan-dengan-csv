import csv
import os
import detail_buku

def apen_data(filename, data):
    with open(filename, mode='a', newline='') as file:
        header = ['Username', 'Judul']
        writer = csv.DictWriter(file, fieldnames=header)

        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(data)


def tambah_buku(user, data_buku):
         
    cart = [{
        'Username' : user['Email'],
        'Judul' : data_buku['Judul']
    }]
    apen_data('keranjang.csv', cart)
    print('Buku Berhasil Ditambahkan ke Keranjang')
    os.system("pause")


def hapus_buku(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        input_hapus = input('Ketikkan Judul Yang Ingin Dihapus: ')
        data = []
        for row in list(reader):
            if row['Judul'].lower() != input_hapus.lower():
                data.append(row)

    with open(filename,mode='w', newline='') as writee:
        writer = csv.DictWriter(writee, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)
        print(f"Buku {input_hapus} Berhasil Dihapus dari Keranjang")
        os.system('pause')

# hapus_buku("keranjang.csv")


def daftar_buku_keranjang():
    with open('keranjang.csv', mode='r') as file:
        reader =list(csv.DictReader(file))
        urutan=0
        for data in reader:
            urutan+=1
            print(f"{urutan}.{data['Judul']}")

        if urutan == 0:
            print("Keranjang anda kosong")


def menu_keranjang():
    while True:
        os.system('cls')
        daftar_buku_keranjang()
        print('\n1.Beli')
        print('2.Hapus')
        print('3.Kembali')

        pilihan_user = input("\nketik angka (1/2/3): ")

        if pilihan_user =='1':
            os.system('cls')
            daftar_buku_keranjang()
        elif pilihan_user =='2':
            daftar_buku_keranjang()
            hapus_buku('keranjang.csv')
            
