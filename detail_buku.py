import csv
from list_buku import read_data_buku

def append_data(filename,data):
    with open(filename, mode='a', newline='') as file:
        header = ['Timestamp','Judul','Status']
        writer = csv.DictWriter(file, fieldnames=header)
        
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(data)

def detail(filename):
    
    read_data_buku('data_buku.csv')
    
    input_detail = input("ketikan judul yang ingin di beli: ")
    with open(filename, mode='r') as file:
        reader = list(csv.DictReader(file))
        
        urutan = 0
        for data in reader:
            urutan += 1
            if input_detail.lower() == data['Judul'].lower():
                print(f"Judul    : {data['Judul']}")
                print(f"Penulis  : {data['Penulis']}")
                print(f"Penerbit : {data['Penerbit']}")
                print(f"Kategori : {data['Kategori']}")
                print(f"Stok     : {data['Stok Barang']}")
                print(f"Harga    : {data['Harga']}\n")
                
                print("1.Beli Sekarang")
                print("2.Masukan Keranjang")
                print("3.Kembali")
                input_beli_kerangjang = input("pilih salah satu (1/2/3): ")
                
                if input_beli_kerangjang == "1":
                    print(f"anda telah membeli {input_detail}")
                    print("mohon tunggu persetujuan dari Owl Book")
                    data = [{
                        'Timestamp' : 'waktunya masih kosong',
                        'Judul' : data['Judul'],
                        'Status' : 'Menunggu Persetujuan'
                    }]
                    
                    append_data('status_pembelian.csv', data)
                    
                elif input_beli_kerangjang == "2":
                    print(f"anda telah memasukan {input_detail} ke keranjang")
                elif input_beli_kerangjang == "3":
                    print(f"kembali")
                else:
                    print("masukan angka yang sesuai")
                                                   
detail('data_buku.csv')