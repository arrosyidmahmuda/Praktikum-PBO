from abc import ABC, abstractmethod

class Supplier:
    def __init__(self, nama_supplier):
        self.nama_supplier = nama_supplier

    def kirim_bahan_baku(self, manufaktur):
        print(f"Supplier {self.nama_supplier} mengirim bahan baku untuk Produksi: {manufaktur.id_produksi}")

class MesinProduksi:
    def __init__(self, nama_mesin):
        self.nama_mesin = nama_mesin
        self.status = "Beroperasi"

    def info_mesin(self):
        return f"Mesin: {self.nama_mesin} ({self.status})"

class Barang(ABC):
    nama_instansi = "SIGMA Logistics Center"
    total_jenis_barang = 0

    def __init__(self, kode_barang, nama_barang, stok_awal, harga):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self._harga = harga 
        self.__stok = 0 
        self.stok = stok_awal

        Barang.total_jenis_barang += 1

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai_baru):
        if not isinstance(nilai_baru, int) or nilai_baru < 0:
            print(f"Stok {self.nama_barang} gagal diubah. Input harus angka positif. (Input: {nilai_baru})")
        else:
            self.__stok = nilai_baru
            print(f"Stok {self.nama_barang}: {self.__stok}")

    @abstractmethod
    def tampilkan_detail(self):
        print(f"[{self.kode_barang}] {self.nama_barang} | Stok: {self.stok} unit | Harga: Rp{self._harga:,}")

    @abstractmethod
    def hitung_biaya_simpan(self):
        pass

    def hitung_nilai_stok(self):
        return self.stok * self._harga

    def cetak_laporan(self):
        self.tampilkan_detail()
        print(f"   Nilai stok: Rp{self.hitung_nilai_stok():,} | Biaya simpan: Rp{self.hitung_biaya_simpan():,}")

    def __str__(self):
        return f"{self.kode_barang} - {self.nama_barang}"

    def __lt__(self, other):
        return self._harga < other._harga

    def __add__(self, other):
        return self.hitung_nilai_stok() + other.hitung_nilai_stok()

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
        return kode.startswith("BRG-") and len(kode) >= 7

class BarangElektronik(Barang):
    def __init__(self, kode_barang, nama_barang, stok_awal, harga, daya_watt):
        super().__init__(kode_barang, nama_barang, stok_awal, harga)
        self.daya_watt = daya_watt

    def tampilkan_detail(self):
        print(f"[ELEKTRONIK - {self.kode_barang}] {self.nama_barang} | Daya: {self.daya_watt}W | Stok: {self.stok} | Harga: Rp{self._harga:,}")

    def hitung_biaya_simpan(self):
        return int(self.hitung_nilai_stok() * 0.01)


class BarangPakaian(Barang):
    def __init__(self, kode_barang, nama_barang, stok_awal, harga, ukuran, bahan):
        super().__init__(kode_barang, nama_barang, stok_awal, harga)
        self.ukuran = ukuran
        self._bahan = bahan

    def tampilkan_detail(self):
        print(f"[PAKAIAN - {self.kode_barang}] {self.nama_barang} (Size: {self.ukuran}, Bahan: {self._bahan}) | Stok: {self.stok} | Harga: Rp{self._harga:,}")

    def hitung_biaya_simpan(self):
        return self.stok * 2000

class Manufaktur:
    nama_instansi = "SIGMA Manufacturing Division"
    total_proses_manufaktur = 0
    standar_mutu = "ISO-9001"

    def __init__(self, id_produksi, produk_jadi, target_produksi):
        self.id_produksi = id_produksi
        self.produk_jadi = produk_jadi 
        self.__target_produksi = 0
        self.target_produksi = target_produksi
        self.mesin_lini = MesinProduksi(f"Robot-Assembly-{self.id_produksi}")

        Manufaktur.total_proses_manufaktur += 1

    @property
    def target_produksi(self):
        return self.__target_produksi

    @target_produksi.setter
    def target_produksi(self, jumlah):
        if not isinstance(jumlah, int) or jumlah <= 0:
            print(f"Target produksi {self.id_produksi} tidak valid. (Input: {jumlah})")
        else:
            self.__target_produksi = jumlah
            print(f"Target produksi {self.id_produksi} diatur: {self.__target_produksi}")

    def proses_produksi(self, jumlah_hasil):
        print(f"\nMemulai produksi ID: {self.id_produksi}...")
        print(f"Menggunakan {self.mesin_lini.info_mesin()}") 
        
        if jumlah_hasil <= 0:
            print("Hasil produksi tidak valid.")
        else:
            print(f"Target: {self.target_produksi} unit | Berhasil diproduksi: {jumlah_hasil} unit")
            self.produk_jadi.stok += jumlah_hasil

    def cetak_status(self):
        print(f"[MANUFAKTUR] {self.id_produksi} | Produk: {self.produk_jadi.nama_barang} | Target: {self.target_produksi} unit | Standar: {self.standar_mutu}")

    @classmethod
    def ubah_standar_mutu(cls, standar_baru):
        cls.standar_mutu = standar_baru
        print(f"Standar mutu pabrik diubah: {cls.standar_mutu}")

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

        ArusBarang.total_transaksi += 1

    @property
    def jumlah_barang(self):
        return self.__jumlah_barang

    @jumlah_barang.setter
    def jumlah_barang(self, jumlah):
        if not isinstance(jumlah, int) or jumlah <= 0:
            print(f"Jumlah transaksi {self.id_transaksi} harus lebih dari 0. (Input: {jumlah})")
        else:
            self.__jumlah_barang = jumlah

    def eksekusi_transaksi(self, jumlah):
        print(f"\nMengeksekusi transaksi {self.jenis_transaksi.upper()} ID: {self.id_transaksi}")
        self.jumlah_barang = jumlah

        if self.jumlah_barang > 0:
            if self.jenis_transaksi.upper() == "MASUK":
                self.barang.stok += self.jumlah_barang
            elif self.jenis_transaksi.upper() == "KELUAR":
                if self.barang.stok >= self.jumlah_barang:
                    self.barang.stok -= self.jumlah_barang
                else:
                    print(f"Transaksi gagal. Stok {self.barang.nama_barang} tidak mencukupi!")

    def cetak_status(self):
        print(f"[ARUS BARANG] {self.id_transaksi} | {self.jenis_transaksi.upper()} | Barang: {self.barang.nama_barang} | Jumlah: {self.jumlah_barang} unit | Layanan: {self.status_layanan}")

    @classmethod
    def set_status_layanan(cls, status_baru):
        cls.status_layanan = status_baru
        print(f"Status layanan logistik diperbarui: {cls.status_layanan}")

    @staticmethod
    def validasi_jenis_transaksi(jenis):
        return jenis.upper() in ["MASUK", "KELUAR"]

def tampilkan_status(objek):
    objek.cetak_status()

if __name__ == "__main__":
    print(f"{Barang.nama_instansi}")
    
    print("\n1. DATA BARANG AWAL")
    barang_elektronik = BarangElektronik("BRG-001", "Laptop Gaming", 10, 15000000, 240)
    barang_pakaian = BarangPakaian("BRG-002", "Jaket Hoodie", 20, 250000, "L", "Fleece Cotton")
    
    barang_elektronik.tampilkan_detail()
    barang_pakaian.tampilkan_detail()

    print("\n2. PROSES MANUFAKTUR")
    manufaktur1 = Manufaktur("MNF-101", barang_elektronik, 50)
    supplier1 = Supplier("PT Sumber Material")
    
    supplier1.kirim_bahan_baku(manufaktur1) 
    manufaktur1.proses_produksi(20)

    print("\n3. PROSES DISTRIBUSI (TRANSAKSI)")
    transaksi1 = ArusBarang("TRX-001", barang_elektronik, "KELUAR")
    transaksi2 = ArusBarang("TRX-002", barang_pakaian, "MASUK")

    transaksi1.eksekusi_transaksi(5)
    transaksi2.eksekusi_transaksi(10)

    print("\n4. BUKTI ABSTRAKSI (ABSTRACT CLASS TIDAK BISA DIINSTANSIASI)")
    try:
        barang_abstrak = Barang("BRG-999", "Barang Abstrak", 1, 1000)
    except TypeError as error:
        print(f"TypeError: {error}")

    print("\n5. POLIMORFISME VIA PEWARISAN")
    daftar_barang = [barang_elektronik, barang_pakaian]
    for barang in daftar_barang:
        barang.cetak_laporan()

    print("\n6. DUCK TYPING")
    for objek in [manufaktur1, transaksi1, transaksi2]:
        tampilkan_status(objek)

    print("\n7. OPERATOR OVERLOADING")
    print(f"__str__ : {barang_elektronik} | {barang_pakaian}")
    print(f"__lt__  : {barang_elektronik.nama_barang} < {barang_pakaian.nama_barang} ? {barang_elektronik < barang_pakaian}")
    print(f"sorted  : {[str(barang) for barang in sorted(daftar_barang)]}")
    print(f"__add__ : Total nilai stok kedua barang = Rp{barang_elektronik + barang_pakaian:,}")

    print("\nRANGKUMAN HASIL AKHIR")
    print(f"Total Jenis Barang      : {Barang.total_jenis_barang}")
    print(f"Total Sesi Pabrik       : {Manufaktur.total_proses_manufaktur}")
    print(f"Total Sesi Transaksi    : {ArusBarang.total_transaksi}")
    print("Detail Barang")
    barang_elektronik.tampilkan_detail()
    barang_pakaian.tampilkan_detail()