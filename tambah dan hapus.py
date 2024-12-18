import csv

def tambah_buku(filename): #fungsi menambah buku
    # menginput buku ke dalam csv
    Judul = input("Masukkan judul: ")
    Penulis = input("Masukkan nama penulis: ")
    Penerbit = input("Masukkan nama penerbit: ")
    Kategori = input("Kategori (Fiksi/Non Fiksi): ").strip()#di bagian ini admin hanya bisa melakukan 2 inputan, yaiut Fiksi/Non-Fiksi
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
            header = ['Id', 'Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
            writer = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:  # Menulis header jika file kosong
                writer.writeheader()
            writer.writerows(new_data) # Menulis baris data yang telah diperbarui
            print(f"Buku dengan judul '{Judul_buku}' telah dihapus.")


tambah_buku('data_buku.csv')

# hapus_buku('data_buku.csv')
