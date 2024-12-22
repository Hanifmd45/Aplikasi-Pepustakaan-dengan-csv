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
    cart = [{'Username': user['Email'], 'Judul': data_buku['Judul']}]
    apen_data('keranjang.csv', cart)
    print(f"\nBuku {data_buku['Judul']} berhasil ditambahkan ke keranjang.")
    os.system("pause")


def hapus_buku(filename, judul, username):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            # Menyaring buku yang tidak sesuai judul dan username
            if row['Judul'].lower() != judul.lower() or row['Username'] != username:
                data.append(row)

    with open(filename, mode='w', newline='') as writee:
        writer = csv.DictWriter(writee, fieldnames=['Username', 'Judul'])
        writer.writeheader()
        writer.writerows(data)
        print(f"Buku {judul} berhasil dihapus dari keranjang.")
        os.system('pause')


def daftar_buku_keranjang(data_user):
    with open('keranjang.csv', mode='r') as file:
        reader = list(csv.DictReader(file))
        urutan = 0
        for data in reader:
            if data['Username'] == data_user['Email']:
                urutan += 1
                print(f"{urutan}. {data['Judul']}")

        if urutan == 0:
            print("|  Keranjang Anda kosong |")
        return urutan


def menu_keranjang(data_user):
    while True:
        os.system('cls')
        print("|========================|")
        print("|---- Menu Keranjang ----|")
        daftar_buku_keranjang(data_user)
        print('\n1. Beli')
        print('2. Hapus')
        print('3. Kembali')
        print("|========================|")

        pilihan_user = input("\nKetik angka (1/2/3): ")

        if pilihan_user == '1':
            os.system('cls')
            if daftar_buku_keranjang(data_user) == 0:
                input("Keranjang kosong. Tekan Enter untuk kembali.")
                continue

            input_detail = input("\nKetikkan judul yang ingin dibeli (atau 'k' untuk kembali): ")
            if input_detail.lower() == 'k':
                continue

            with open('data_buku.csv', mode='r') as file:
                reader = list(csv.DictReader(file))
                for data in reader:
                    if input_detail.lower() == data['Judul'].lower():
                        detail_buku.detail_buku(data)

                        print(f"Saldo Anda sekarang: {data_user['Saldo']}")
                        print("1. Beli Sekarang")
                        print("2. Kembali")
                        input_beli = input("Pilih salah satu (1/2): ")

                        if input_beli == '1':
                            if int(data['Stok Barang']) <= 0:
                                print(f"Maaf, stok buku {data['Judul']} habis")
                                os.system('pause')
                                break

                            elif int(data_user['Saldo']) < int(data['Harga']):
                                print("Saldo tidak cukup untuk melakukan pembelian")
                                os.system('pause')
                                break

                            else:
                                detail_buku.pembayaran('data_pelanggan.csv', data, data_user)

                                updated_user = detail_buku.refresh_user_data('data_pelanggan.csv', data_user['Email'])
                                if updated_user:
                                    data_user.update(updated_user)

                                hapus_buku('keranjang.csv', data['Judul'], data_user['Email'])
                                break
                        elif input_beli == '2':
                            break
                        else:
                            print("Masukkan angka yang sesuai")
                            os.system('pause')
                            break
                else:
                    print("\nBuku tidak ditemukan")
                    input("Tekan Enter untuk kembali")
        elif pilihan_user == '2':
            os.system('cls')
            if daftar_buku_keranjang(data_user) == 0:
                input("Keranjang kosong, Tekan Enter untuk kembali")
                continue

            input_hapus = input("Ketikkan judul buku yang ingin dihapus: ")
            hapus_buku('keranjang.csv', input_hapus, data_user['Email'])
        elif pilihan_user == '3':
            return
        else:
            print("Mohon inputkan angka yang sesuai (1/2/3).")
            os.system('pause')
