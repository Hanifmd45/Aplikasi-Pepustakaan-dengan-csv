import csv

def tambah_buku(filename): #fungsi menambah buku
    # menginput buku ke dalam csv
    Judul = input("Masukkan judul: ")
    Penulis = input("Masukkan nama penulis: ")
    Penerbit = input("Masukkan nama penerbit: ")
    Kategori = input("Masukkan kategori: ")
    Stok_Barang = input("Masukkan jumlah buku: ")
    Harga = input("Masukkan harga buku: ")
    
    with open (filename, mode="a", newline='') as file: #menulis buku yang sudah di input
        header = ['Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
        writer = csv.DictWriter(file, fieldnames=header)
        if file.tell() == 0:  # Menulis header jika file kosong
                writer.writeheader()
        # menulis baris baru yang berisi informasi buku
        writer.writerow({
            'Judul': Judul,
            'Penerbit': Penerbit,
            'Penulis': Penulis,
            'Kategori': Kategori,
            'Stok Barang' : Stok_Barang,
            'Harga' : Harga
             })
        print(f"Buku {Judul} Berhasil di tambah")
        
def hapus_buku(filename): #fungsi menghapus buku
    Judul_buku = input("Masukkan Judul yang ingin di hapus: ") # Inputan untuk menghapus buku
    with open(filename, mode='r', newline='', encoding='utf-8') as file:# Membaca file dan mengambil data buku
        reader = csv.DictReader(file)
        data = list(reader)
    
    # Menyaring data buku yang sesuai dengan Judul_buku
    new_data = [row for row in data if row['Judul'] != Judul_buku]
    
    if len(new_data) == len(data): # Mengecek apakah ada perubahan
        print(f"Judul buku '{Judul_buku}' tidak tersedia.")
    else:
        with open(filename, mode='w', newline='', encoding='utf-8') as file: # Menyimpan data yang telah diperbarui ke file CSV
            header = ['Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
            writer = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:  # Menulis header jika file kosong
                writer.writeheader()
            writer.writerows(new_data) # Menulis baris data yang telah diperbarui
            print(f"Buku dengan judul '{Judul_buku}' telah dihapus.")


# tambah_buku('data_buku.csv')

hapus_buku('data_buku.csv')