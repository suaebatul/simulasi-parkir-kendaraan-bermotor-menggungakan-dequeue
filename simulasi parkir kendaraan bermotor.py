from collections import deque

class Parkir:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.kendaraan = deque()

    def masuk(self, plat_nomor):
        if len(self.kendaraan) < self.kapasitas:
            self.kendaraan.append(plat_nomor)
            print(f"Kendaraan dengan plat nomor {plat_nomor} telah masuk ke parkir.")
        else:
            print("Parkir penuh, tidak dapat masuk.")

    def keluar(self, plat_nomor):
        if plat_nomor in self.kendaraan:
            self.kendaraan.remove(plat_nomor)
            print(f"Kendaraan dengan plat nomor {plat_nomor} telah keluar dari parkir.")
        else:
            print("Kendaraan tidak ditemukan di parkir.")

    def lihat_kendaraan(self):
        print("Kendaraan yang sedang parkir:")
        for i, plat_nomor in enumerate(self.kendaraan):
            print(f"{i+1}. {plat_nomor}")

    def jumlah_kendaraan(self):
        return len(self.kendaraan)

parkir = Parkir(5)

while True:
    print("\nMenu:")
    print("1. Masuk kendaraan")
    print("2. Keluar kendaraan")
    print("3. Lihat kendaraan")
    print("4. Jumlah kendaraan")
    print("5. Keluar program")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        plat_nomor = input("Masukkan plat nomor kendaraan: ")
        parkir.masuk(plat_nomor)
    elif pilihan == "2":
        plat_nomor = input("Masukkan plat nomor kendaraan: ")
        parkir.keluar(plat_nomor)
    elif pilihan == "3":
        parkir.lihat_kendaraan()
    elif pilihan == "4":
        print(f"Jumlah kendaraan: {parkir.jumlah_kendaraan()}")
    elif pilihan == "5":
        break
    else:
        print("Menu tidak tersedia.")
