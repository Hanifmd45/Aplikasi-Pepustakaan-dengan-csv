import csv

# log = "data_buku.csv"
# data = {}

def tambah_buku(filename):
    Judul = input("Masukkan judul: ")
    Penulis = input("Masukkan nama penulis: ")
    Penerbit = input("Masukkan nama penerbit: ")
    Kategori = input("Masukkan kategori: ")
    Stok_Barang = input("Masukkan jumlah buku: ")
    Harga = input("Masukkan harga buku: ")
    with open (filename, mode="a", newline='') as file:
        header = ['Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerow({
            'Judul': Judul,
            'Penerbit': Penerbit,
            'Penulis': Penulis,
            'Kategori': Kategori,
            'Stok Barang' : Stok_Barang,
            'Harga' : Harga
             })
        print(f"Buku {Judul} Berhasil di tambah")
        
        
def hapus_buku(filename):
    Judul = input("Masukkan Judul yang ingin di hapus: ")
    with open(filename, mode='r', newline='', encoding='utf-8') as file :
        reader = csv.DictReader(file)           
        data = list(reader)      
         
        new_data = [row for row in data if row ['Judul'] != Judul]    
        
    if len(new_data) == len(data):
        print(f"Judul buku {Judul} tidak tersedia.")
    else:
        with open (filename, mode='w', newline='') as file:
            header = ['Judul', 'Penulis', 'Penerbit', 'Kategori', 'Stok Barang', 'Harga']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader
            writer.writerows(new_data)
            
            print(f"buku {Judul} telah di hapus")

# tambah_buku('data_buku.csv')

hapus_buku('data_buku.csv')