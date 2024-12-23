import csv
import os
from daftar_buku import list_data_buku

def tambah_buku_baru(filename): #fungsi menambah buku
    # menginput buku ke dalam csv
    Judul = input("Masukkan judul: ")
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # Membaca seluruh data buku

    # Pengecekan judul, apakah double atau tidak
    for item in data:
        if item['Judul'].lower() == Judul.lower():
            print(f"Buku dengan judul '{Judul}' sudah ada di dalam daftar")
            os.system('pause')
            return
            
    Penulis = input("Masukkan nama penulis: ")
    Penerbit = input("Masukkan nama penerbit: ")
    Kategori = input("Kategori (Fiksi/Non-Fiksi): ").strip()#di bagian ini admin hanya bisa melakukan 2 inputan, yaiut Fiksi/Non-Fiksi
    while Kategori not in ["Fiksi", "Non-Fiksi"]:
        print("Kategori salah! Silakan pilih Fiksi atau Non-Fiksi.")
        Kategori = input("Kategori: ").strip()    
    Stok_Barang = input("Masukkan jumlah buku: ")
    Harga = input("Masukkan harga buku: ")
    
    try: 
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            if data:
                last = int(data[-1]['Id'])
                Id = last + 1
            else:
                Id = 1
    except FileNotFoundError:
        Id = 1      
        
    with open (filename, mode="a", newline='', encoding='utf-8') as file: #menulis buku yang sudah di input
        header = ['Id','Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
        writer = csv.DictWriter(file, fieldnames=header)
        if file.tell() == 0:  # Menulis header jika file kosong
                writer.writeheader()
        # menulis baris baru yang berisi informasi buku
        writer.writerow({
            'Id' : Id,
            'Judul': Judul,
            'Penerbit': Penerbit,
            'Penulis': Penulis,
            'Kategori': Kategori,
            'Stok Barang' : Stok_Barang,
            'Harga' : Harga
                })
        print(f"Buku {Judul} Dengan Id {Id} Berhasil di tambahkan")
        os.system('pause')
        
def ubah_stok(filename):
    list_data_buku()
    Judul_buku = input("Masukkan Judul buku yang stoknya ingin di ubah: ")
    
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # Membaca seluruh data buku

    cari_buku = False
    for row in data:
        if row['Judul'].lower() == Judul_buku.lower(): #mencocokkan judul buku
            cari_buku = True
            print(f"Buku ditemukan: {row['Judul']} Dengan stok barang saat ini: {row['Stok Barang']}")
            stok_baru = input("Masukkan jumlah stok yang baru: ")
            row['Stok Barang'] = stok_baru
            break
        
    if not cari_buku:
            print(f"Buku dengan judul '{Judul_buku}' tidak ditemukan.")
            os.system('pause')
            return  # Menghentikan fungsi jika buku tidak ditemukan 
            # Tulis ulang data ke file
            
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Id', 'Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()  # Menulis header file
        writer.writerows(data)  # Menulis ulang data buku
        print(f"Stok buku '{Judul_buku}' berhasil diubah.")
        os.system('pause')
        
        
def ubah_harga(filename):
    list_data_buku()
    Judul_buku = input("Masukkan Judul buku yang harganya ingin di ubah: ")
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # Membaca seluruh data buku

    cari_buku = False
    for row in data:
        if row['Judul'].lower() == Judul_buku.lower(): #mencocokkan judul buku
            cari_buku = True
            print(f"Buku ditemukan: {row['Judul']} Dengan stok barang saat ini: {row['Harga']}")
            Harga_baru = input("Masukkan Harga buku yang baru: ")
            row['Harga'] = Harga_baru
            break
    if not cari_buku:
        print(f"Buku dengan judul '{Judul_buku}' tidak ditemukan.")
        os.system('pause')
        return  # Menghentikan fungsi jika buku tidak ditemukan   
            # Tulis ulang data ke file
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Id', 'Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()  # Menulis header file
        writer.writerows(data)  # Menulis ulang data buku
        print(f"Harga buku '{Judul_buku}' berhasil diubah.")
        os.system('pause')
        
        
        
def hapus_buku(filename): #fungsi menghapus buku
    list_data_buku()
    Judul_buku = input("Masukkan Judul yang ingin di hapus: ") # Inputan untuk menghapus buku
    with open(filename, mode='r', newline='', encoding='utf-8') as file:# Membaca file dan mengambil data buku
        reader = csv.DictReader(file)
        data = list(reader)
    
    # Menyaring data buku yang sesuai dengan Judul_buku
    new_data = [row for row in data if row['Judul'] != Judul_buku]
     
    if len(new_data) == len(data): # Mengecek apakah ada perubahan
        print(f"Judul buku '{Judul_buku}' tidak tersedia.")
        os.system('pause')
    else:
        with open(filename, mode='w', newline='', encoding='utf-8') as file: # Menyimpan data yang telah diperbarui ke file CSV
            header = ['Id', 'Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
            writer = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:  # Menulis header jika file kosong
                writer.writeheader()
            writer.writerows(new_data) # Menulis baris data yang telah diperbarui
            print(f"Buku dengan judul '{Judul_buku}' telah dihapus.")
            os.system('pause')
            
def tambah_buku():
    print("0.Kembali")
    print("1.Tambah buku")
    print("2.Update Stok")
    print("3.Update Harga")
    pilih = input("Pilih opsi: ")
    
    if pilih == '1':
        tambah_buku_baru('data_buku.csv')
    elif pilih == '2':
        ubah_stok('data_buku.csv')
    elif pilih == '3':
        ubah_harga('data_buku.csv')
    elif pilih == '0':
        return
    else:
        print("tolong masukan angka sesuai menu yang ada")
        
# tambah_buku('data_buku.csv')

# hapus_buku('data_buku.csv')

# ubah_harga('data_buku.csv')