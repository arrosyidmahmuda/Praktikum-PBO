class Barang:
    nama_instansi = "SIGMA Logistics Center"
    total_jenis_barang = 0

    def __init__(self, kode_barang, nama_barang, stok_awal, harga):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.harga = harga
        self.__stok = 0
        self.stok = stok_awal

        Barang.total_jenis_barang = Barang.total_jenis_barang + 1

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai_baru):
        if type(nilai_baru) != int or nilai_baru < 0:
            print(f"[Ups, Gagal!] Stok {self.nama_barang} gak boleh minus atau aneh-aneh! (Input: {nilai_baru})")
        else:
            self.__stok = nilai_baru
            print(f"[Sip!] Stok {self.nama_barang} berhasil diupdate jadi: {self.__stok}")

    def tampilkan_detail(self):
        print(f"[{self.kode_barang}] {self.nama_barang} | Stok: {self.stok} unit | Harga: Rp{self.harga:,}")

    @classmethod
    def dari_dictionary(cls, data_dict):
        return cls(
            kode_barang=data_dict["kode"],
            nama_barang=data_dict["nama"],
            stok_awal=data_dict["stok"],
            harga=data_dict["harga"]
        )

    @staticmethod
    def validasi_kode_barang(kode):
        if kode.startswith("BRG-") and len(kode) >= 7:
            return True
        else:
            return False

class Manufaktur:
    nama_instansi = "SIGMA Manufacturing Division"
    total_proses_manufaktur = 0
    standar_mutu = "ISO-9001"

    def __init__(self, id_produksi, produk_jadi, target_produksi):
        self.id_produksi = id_produksi
        self.produk_jadi = produk_jadi
        self.__target_produksi = 0
        self.target_produksi = target_produksi

        Manufaktur.total_proses_manufaktur = Manufaktur.total_proses_manufaktur + 1

    @property
    def target_produksi(self):
        return self.__target_produksi

    @target_produksi.setter
    def target_produksi(self, jumlah):
        if type(jumlah) != int or jumlah <= 0:
            print(f" [Gagal] Target produksi {self.id_produksi} harus angka diatas 0! (Input: {jumlah})")
        else:
            self.__target_produksi = jumlah
            print(f" [Sip!] Target produksi {self.id_produksi} diset jadi: {self.__target_produksi}")

    def proses_produksi(self, jumlah_hasil):
        print(f"\n Lagi memproses produksi ID: {self.id_produksi}...")
        if jumlah_hasil <= 0:
            print(" Hasil produksi gak valid nih!")
        else:
            print(f"Target: {self.target_produksi} unit | Berhasil dibuat: {jumlah_hasil} unit")
            self.produk_jadi.stok = self.produk_jadi.stok + jumlah_hasil

    @classmethod
    def ubah_standar_mutu(cls, standar_baru):
        cls.standar_mutu = standar_baru
        print(f" [Info Kelas] Standar mutu pabrik diganti jadi: {cls.standar_mutu}")

    @staticmethod
    def hitung_estimasi_waktu(jumlah_unit, kecepatan_per_jam):
        if kecepatan_per_jam <= 0:
            return 0
        return jumlah_unit / kecepatan_per_jam

class ArusBarang:
    nama_instansi = "SIGMA Logistics & Distribution"
    total_transaksi = 0
    status_layanan = "Aktif"

    def __init__(self, id_transaksi, barang, jenis_transaksi):
        self.id_transaksi = id_transaksi
        self.barang = barang
        self.jenis_transaksi = jenis_transaksi
        self.__jumlah_barang = 0

        ArusBarang.total_transaksi = ArusBarang.total_transaksi + 1

    @property
    def jumlah_barang(self):
        return self.__jumlah_barang

    @jumlah_barang.setter
    def jumlah_barang(self, jumlah):
        if type(jumlah) != int or jumlah <= 0:
            print(f" [Gagal] Jumlah transaksi {self.id_transaksi} harus angka positif! (Input: {jumlah})")
        else:
            self.__jumlah_barang = jumlah
            print(f" [Sip!] Jumlah barang transaksi {self.id_transaksi} diset ke: {self.__jumlah_barang}")

    def eksekusi_transaksi(self, jumlah):
        print(f"\n Menjalankan Transaksi [{self.jenis_transaksi}] ID: {self.id_transaksi}")
        self.jumlah_barang = jumlah

        if self.jumlah_barang > 0:
            if self.jenis_transaksi.upper() == "MASUK":
                self.barang.stok = self.barang.stok + self.jumlah_barang
            elif self.jenis_transaksi.upper() == "KELUAR":
                if self.barang.stok >= self.jumlah_barang:
                    self.barang.stok = self.barang.stok - self.jumlah_barang
                else:
                    print(f" [Gagal] Stok {self.barang.nama_barang} gak cukup buat dikeluarkan!")

    @classmethod
    def set_status_layanan(cls, status_baru):
        cls.status_layanan = status_baru
        print(f" [Info Kelas] Status layanan logistik diganti jadi: {cls.status_layanan}")

    @staticmethod
    def validasi_jenis_transaksi(jenis):
        if jenis.upper() == "MASUK" or jenis.upper() == "KELUAR":
            return True
        else:
            return False

if __name__ == "__main__":
    print("==================================================================")
    print(f"                 {Barang.nama_instansi}")
    print("==================================================================\n")
    print("--- 1. TES CLASS BARANG ---")
    
    barang1 = Barang("BRG-001", "Laptop Gaming", 10, 15000000)
    data_mouse = {"kode": "BRG-002", "nama": "Mouse Wireless", "stok": 20, "harga": 250000}
    barang2 = Barang.dari_dictionary(data_mouse)

    print("\n* Cek Static Method (Validasi Format Kode) *")
    print("Kode 'BRG-001' benar?:", Barang.validasi_kode_barang("BRG-001"))
    print("Kode 'LPT-123' benar?:", Barang.validasi_kode_barang("LPT-123"))
    print("\n* Data Barang Saat Ini *")

    barang1.tampilkan_detail()
    barang2.tampilkan_detail()

    print("\n* Tes Setter Stok Barang *")
    print("Input yang bener (isi 15):")
    barang1.stok = 15

    print("Input salah (isi minus -5):")
    barang1.stok = -5

    print("Input salah (isi tulisan 'banyak'):")
    barang1.stok = "banyak"

    print("\n\n--- 2. TES CLASS MANUFAKTUR ---")

    manufaktur1 = Manufaktur("MNF-101", barang1, 50)
    manufaktur2 = Manufaktur("MNF-102", barang2, 100)

    Manufaktur.ubah_standar_mutu("ISO-9001:2026")

    waktu = Manufaktur.hitung_estimasi_waktu(200, 50)
    print(f"* Static Method *: Estimasi bikin 200 unit = {waktu} jam")

    manufaktur1.proses_produksi(20)

    print("\n* Tes Setter Target Produksi *")
    print("Input bener:")
    manufaktur2.target_produksi = 150

    print("Input salah (angka 0):")
    manufaktur2.target_produksi = 0

    print("\n\n--- 3. TES CLASS ARUS BARANG ---")
    
    transaksi1 = ArusBarang("TRX-001", barang1, "KELUAR")
    transaksi2 = ArusBarang("TRX-002", barang2, "MASUK")

    ArusBarang.set_status_layanan("Maintenance")
    print("* Static Method *: Jenis 'MASUK' valid?:", ArusBarang.validasi_jenis_transaksi("MASUK"))

    transaksi1.eksekusi_transaksi(5)
    transaksi2.eksekusi_transaksi(10)

    print("\n* Tes Setter Jumlah Transaksi *")
    print("Input bener:")
    transaksi1.jumlah_barang = 30
    print("Input salah (angka minus):")
    transaksi1.jumlah_barang = -10

    print("\n==================================================================")
    print("RANGKUMAN HASIL AKHIR")
    print("==================================================================")
    print("Total Jenis Barang :", Barang.total_jenis_barang)
    print("Total Sesi Pabrik   :", Manufaktur.total_proses_manufaktur)
    print("Total Transaksi     :", ArusBarang.total_transaksi)
    print("------------------------------------------------------------------")
    barang1.tampilkan_detail()
    barang2.tampilkan_detail()
    print("==================================================================")