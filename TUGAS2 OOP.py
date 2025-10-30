class SepedaMotor:
    #  Class variable
    jenis_kendaraan = "Sepeda Motor"
    jumlah_motor = 0  # untuk menghitung berapa banyak objek motor dibuat

    def _init_(self, merk, model, cc, tahun, warna, surat):
        #  Instance variable
        self.merk = merk
        self.model = model
        self.cc = cc
        self.tahun = tahun
        self.warna = warna
        self.surat = surat  

        # Tambahkan penghitung setiap kali objek dibuat
        SepedaMotor.jumlah_motor += 1

    def tampilkan_info(self):
        print(f"Jenis: {SepedaMotor.jenis_kendaraan}")
        print(f"Motor: {self.merk} {self.model}")
        print(f"CC: {self.cc} | Tahun: {self.tahun} | Warna: {self.warna}")
        print(f"Surat yang dimiliki: {', '.join(self.surat)}")
        print("-" * 30)

# Membuat objek motor (instance)
motor1 = SepedaMotor(
    merk="Honda",
    model="Beat",
    cc="110",
    tahun="2022",
    warna="Merah",
    surat=["STNK", "BPKB", "Asuransi"]
)

motor2 = SepedaMotor(
    merk="Yamaha",
    model="Mio",
    cc="125",
    tahun="2021",
    warna="Hitam",
    surat=["STNK", "BPKB"]
)

print("Daftar Sepeda Motor:")
motor1.tampilkan_info()
motor2.tampilkan_info()

#  Menampilkan class variable
print(f"Total motor yang terdaftar: {SepedaMotor.jumlah_motor}")
