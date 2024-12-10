import csv

def list_data_buku(filename):
    with open(filename, mode='r') as file:
        reader = list(csv.DictReader(file))
        
        urutan = 0
        for data in reader:
            urutan += 1
            print(f"{urutan}.{data['Judul']}")

def filter_data_buku(filename):
    with open(filename, mode='r') as file:
        reader = list(csv.DictReader(file))
        
        print("1.Fiksi")    
        print("2.Non-Fiksi")    
        input_kategori = input("masukan kategori buku yang ingin beli (1/2): ")
        urutan = 0
        for data in reader:
            if input_kategori == '1':
                if data['Kategori'] == "Fiksi":
                    urutan += 1
                    print(f"{urutan}.{data['Judul']}")        
            elif input_kategori == "2":
                if data['Kategori'] == "Non-fiksi":
                    urutan += 1
                    print(f"{urutan}.{data['Judul']}") 
            else:
                print("Mohon inputan angka yang sesuai")
                       
filter_data_buku('data_buku.csv')

        


