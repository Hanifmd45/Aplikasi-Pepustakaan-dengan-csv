import csv
import daftar_buku 
import keranjang
import os

def append_data(filename,data):
    with open(filename, mode='a', newline='') as file:
        header = ['Username','Timestamp','Judul','Harga','Status']
        writer = csv.DictWriter(file, fieldnames=header)
        
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(data)

# sebuah function untuk merefresh variabel user dari function user_login 
# dengan data yang baru setelah melakukan pembelian  
def refresh_user_data(filename, email):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            if item["Email"] == email:
                return {'Email': item["Email"], 'Saldo': item['Saldo']}
    return None

def update_stok_barang(filename, judul_buku):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # Membaca seluruh data buku

    # Perbarui stok barang
    for item in data:
        if item['Judul'].lower() == judul_buku.lower():
            sisa_stok = int(item['Stok Barang']) - 1
            item['Stok Barang'] = str(sisa_stok)  # Perbarui stok

    # Tulis ulang data ke file
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Id', 'Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Menulis header file
        writer.writerows(data)  # Menulis ulang data buku


# sebuah function untuk menambahakan data ke status pembelian 
# dan dan merubah data saldo dari user bila pembelian berhasil
def pembayaran(filename, data_buku,target_email):
    sisa_saldo = int(target_email['Saldo']) - int(data_buku['Harga'])

    print(f"\nanda telah membeli {data_buku['Judul']}")
    print(f"Sisa saldo : {sisa_saldo}")
    print("mohon tunggu persetujuan dari Owl Book")
    input("klik enter untuk lanjut")

    data_baru = [{
        'Username' : target_email['Email'] or 'guest',
        'Timestamp' : 'waktunya masih kosong',
        'Judul' : data_buku['Judul'],
        'Harga' : data_buku['Harga'],
        'Status' : 'Menunggu Persetujuan'
    }]

    append_data('status_pembelian.csv', data_baru)


    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

        # merubah saldo user setelah membeli buku
        for item in data:
            if item['Email'] == target_email['Email']:
                item['Saldo'] = str(sisa_saldo)

        with open(filename, mode='w', newline='') as file:
            fieldnames = ['Email', 'Password', 'Saldo']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
        
            writer.writeheader()  
            writer.writerows(data) 

    update_stok_barang('data_buku.csv', data_buku['Judul'])

def detail_buku(data):
    os.system('cls')
    print(f"|Judul    : {data['Judul']}")
    print(f"|Penulis  : {data['Penulis']}")
    print(f"|Penerbit : {data['Penerbit']}")
    print(f"|Kategori : {data['Kategori']}")
    print(f"|Stok     : {data['Stok Barang']}")
    print(f"|Harga    : {data['Harga']}\n")

def detail(filename,item=None):
    with open(filename, mode='r') as file:
        reader = list(csv.DictReader(file))

        print("\nketik k untuk kembali")
        input_detail = input("ketikan judul yang ingin di beli: ")
        os.system('cls')

        if input_detail == "k":
            # untuk menghentikan function detail()
            return

        for data in reader:
            if input_detail.lower() == data['Judul'].lower():
                detail_buku(data)
                
                print(f"Saldo anda sekarang: {item['Saldo']}")
                print("1.Beli Sekarang")
                print("2.Masukan Keranjang")
                print("3.Kembali")
                input_beli_kerangjang = input("pilih salah satu (1/2/3): ")
                
                if input_beli_kerangjang == "1":
                    
                    if int(data['Stok Barang']) <= 0:
                        print(f"Maaf,stok buku {data['Judul']} habis")
                        os.system('pause')
                        break

                    elif int(item['Saldo']) < int(data['Harga']):
                        print("Saldo tidak cukup untuk melakukan pembelian.")
                        os.system('pause')
                        break

                    else:
                        # memanggil function pembayaran dengan data buku dari "for data in reader"
                        # item dari variabel user yang sudah berhasil login
                        pembayaran('data_pelanggan.csv', data, item)

                        updated_user = refresh_user_data('data_pelanggan.csv', item['Email'])
                        if updated_user:
                            item.update(updated_user)
                        break

                elif input_beli_kerangjang == "2":
                    print(f"anda telah memasukan {data['Judul']} ke keranjang")
                    keranjang.tambah_buku(item,data)
                    input("klik enter untuk lanjut")
                elif input_beli_kerangjang == "3":
                    break
                else:
                    print("masukan angka yang sesuai")

        else:
            print("mohon maaf,judul buku tidak ditemukan")
            input("klik enter untuk lanjut")
                     
# untuk menampilkan semua status pemesanan user
def lihat_status_pembelian(item):
    with open('status_pembelian.csv', mode='r') as file:
        reader = list(csv.DictReader(file))

        print("=========================")
        print("--Menu status pemesanan--")
        print("=========================")
        print("")
        urutan = 0
        for data in reader:
            if item['Email'] == data['Username']:
                urutan += 1
                print(f"{urutan}.{data['Judul']} {data['Status']}")
    
        os.system('pause')

def menu_pelanggan(data_user):
    while True:
        os.system('cls')
        print("|====================|") 
        print("|-----Menu utama-----|")
        print("|                    |")
        print("|1.Lihat daftar buku |")
        print("|2.Filter list buku  |")
        print("|3.Lihat Keranjang   |")
        print("|4.Status pembelian  |")
        print("|5.Log-out           |")
        print("|====================|") 

        pilihan_user = input("\nketik angka (1/2/3/4): ")

        if pilihan_user == "1":
            os.system('cls')
            daftar_buku.list_data_buku()
            detail('data_buku.csv',data_user)
        elif pilihan_user == "2":
            os.system('cls')
            daftar_buku.filter_data_buku()
            detail('data_buku.csv',data_user)
        elif pilihan_user == "3":
            keranjang.menu_keranjang()
        elif pilihan_user == "4":
            os.system('cls')
            lihat_status_pembelian(data_user)    
        elif pilihan_user == "5":
            return
        else:
            print("Mohon masukan angka yang sesuai (1/2/3/4)")
            os.system('pause')