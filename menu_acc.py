import csv
import os

def lihat_status_pembelian_admin(filename):
    """
    Menampilkan semua pesanan dari file CSV beserta opsi untuk mengubah statusnya.
    """
    while True:
        os.system('cls')
        print("===== Daftar Pesanan =====")

        with open(filename, mode='r') as file:
            reader = list(csv.DictReader(file))
            urutan = 0
            for i, pesanan in enumerate(reader, start=1):
                urutan += 1
                print(f"{urutan}. Username: {pesanan['Username']}, Judul: {pesanan['Judul']}, "
                      f"Harga: {pesanan['Harga']}, Status: {pesanan['Status']}")

        if urutan == 0:
            print("Tidak ada pesanan.")
            input("Tekan Enter untuk kembali.")
            return

        print("\nPilih opsi:")
        print("1. ACC Pesanan")
        print("2. Kembali")

        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == "1":
            acc_pesanan(filename)
        elif pilihan == "2":
            return
        else:
            print("Masukkan angka yang valid.")
            os.system('pause')

def acc_pesanan(filename):
    """
    Mengubah status pesanan berdasarkan input admin.
    """
    os.system('cls')
    print("===== ACC Pesanan =====")

    with open(filename, mode='r') as file:
        reader = list(csv.DictReader(file))
        urutan = 0
        for i, pesanan in enumerate(reader, start=1):
            urutan += 1
            print(f"{urutan}. Username: {pesanan['Username']}, Judul: {pesanan['Judul']}, "
                  f"Harga: {pesanan['Harga']}, Status: {pesanan['Status']}")

    if urutan == 0:
        print("Tidak ada pesanan untuk diproses.")
        input("Tekan Enter untuk kembali.")
        return

    nomor = input("Masukkan nomor pesanan yang ingin di-ACC: ")

    if not nomor.isdigit():
        print("Masukkan nomor yang valid.")
        input("Tekan Enter untuk kembali.")
        return

    nomor = int(nomor)
    if 1 <= nomor <= len(reader):
        pesanan = reader[nomor - 1]
        print(f"Pesanan yang dipilih: {pesanan['Judul']} (Status: {pesanan['Status']})")
        print("1. Setujui")
        print("2. Tolak")
        print("3. Batal")

        keputusan = input("Masukkan pilihan (1/2/3): ")
        if keputusan == "1":
            reader[nomor - 1]['Status'] = "Disetujui"
            print("Pesanan berhasil disetujui.")
        elif keputusan == "2":
            reader[nomor - 1]['Status'] = "Ditolak"
            print("Pesanan berhasil ditolak.")
        elif keputusan == "3":
            print("Tidak ada perubahan pada pesanan.")
        else:
            print("Masukkan angka yang valid.")
    else:
        print("Nomor pesanan tidak valid.")

    # Menulis ulang data ke file setelah update
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Username', 'Timestamp', 'Judul', 'Harga', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)

    input("Tekan Enter untuk kembali.")

lihat_status_pembelian_admin('status_pembelian.csv')