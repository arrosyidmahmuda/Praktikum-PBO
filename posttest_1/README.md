# Laporan Praktikum Pemrograman Berorientasi Objek
## SIGMA (Sistem Informasi Gudang, Manufaktur dan Arus Barang)

Dokumentasi ini berisi penjelasan struktur kelas, arsitektur program, dan panduan pengujian untuk program manajemen logistik SIGMA yang ditulis dalam file `praktikum1.py`.

---

### 1. Deskripsi Program
Program SIGMA adalah simulasi sistem informasi berbasis Pemrograman Berorientasi Objek (OOP) dengan Python. Program ini mengelola data inventaris barang, target produksi manufaktur, dan pencatatan arus masuk/keluar barang di gudang. Program ini telah menerapkan konsep OOP secara komprehensif, meliputi penggunaan Instance Attribute, Class Attribute, Encapsulation (melalui Private Attribute dan Property/Setter), serta implementasi Instance Method, Class Method, dan Static Method.

---

### 2. Struktur Class dan Arsitektur
Program ini terdiri dari tiga kelas utama yang saling berinteraksi[cite: 5]:

#### A. Class "Barang"
Berfungsi sebagai cetak biru untuk entitas barang di gudang logistik.
*   **Atribut Kelas:** `nama_instansi` bernilai "SIGMA Logistics Center" dan `total_jenis_barang` untuk melacak jumlah variasi barang[cite: 5].
*   **Atribut Instance:** `kode_barang`, `nama_barang`, `harga`, dan atribut *private* `__stok`.
*   **Encapsulation:** Akses ke `__stok` diatur menggunakan `@property` dan `@stok.setter` yang memvalidasi agar input berupa integer dan tidak bernilai negatif.
*   **Method Utama:** 
    *   `tampilkan_detail()`: *Instance method* untuk mencetak rincian barang.
    *   `dari_dictionary()`: *Class method* yang bertindak sebagai *alternative constructor* untuk membuat instansiasi objek dari struktur data dictionary.
    *   `validasi_kode_barang()`: *Static method* untuk memverifikasi apakah kode barang diawali dengan "BRG-" dan memiliki panjang minimal 7 karakter.

> 📸 **Dokumentasi Output Class Barang:**
> ![Screenshot Output Tes Barang](https://github.com/arrosyidmahmuda/Praktikum-PBO/blob/6caf4136ffe0e17583c82bfa6b80eff81804347a/posttest_1/Cuplikan%20layar%202026-09-23%20184917.png)
> *1. TES CLASS BARANG*

#### B. Class "Manufaktur".
Mewakili divisi yang menangani proses perakitan atau produksi barang.
*   **Atribut Kelas:** `nama_instansi` bernilai "SIGMA Manufacturing Division", `total_proses_manufaktur`, dan `standar_mutu` bernilai "ISO-9001".
*   **Atribut Instance:** `id_produksi`, `produk_jadi` (menyimpan referensi objek `Barang`), dan atribut *private* `__target_produksi`.
*   **Encapsulation:** Nilai target divalidasi oleh `@target_produksi.setter` agar selalu bertipe integer dan bernilai di atas 0.
*   **Method Utama:**
    *   `proses_produksi()`: *Instance method* yang mengeksekusi produksi dan secara otomatis menambahkan hasilnya ke properti `stok` pada objek `Barang` terkait.
    *   `ubah_standar_mutu()`: *Class method* untuk memperbarui atribut kelas `standar_mutu`.
    *   `hitung_estimasi_waktu()`: *Static method* untuk mengkalkulasi waktu produksi berdasarkan jumlah unit dan kecepatan per jam.

> 📸 **Dokumentasi Output Class Manufaktur:**
> ![Screenshot Output Tes Manufaktur](https://github.com/arrosyidmahmuda/Praktikum-PBO/blob/65394cc41f07d7fbbb4a68b70f7e556421553149/posttest_1/Cuplikan%20layar%202026-09-23%20184943.png)
>2. TES CLASS MANUFAKTUR

#### C. Class "ArusBarang"
Mengatur dan mencatat lalu lintas barang, baik yang masuk ke maupun keluar dari gudang.
*   **Atribut Kelas:** `nama_instansi` bernilai "SIGMA Logistics & Distribution", `total_transaksi`, dan `status_layanan` bernilai "Aktif".
*   **Atribut Instance:** `id_transaksi`, `barang` (menyimpan referensi objek `Barang`), `jenis_transaksi`, dan atribut *private* `__jumlah_barang`.
*   **Encapsulation:** Nilai kuantitas transaksi dijaga oleh `@jumlah_barang.setter` agar harus berupa angka positif.
*   **Method Utama:**
    *   `eksekusi_transaksi()`: *Instance method* yang memverifikasi kecukupan stok; akan menambah `stok` barang jika jenis transaksi "MASUK", dan mengurangi `stok` jika "KELUAR".
    *   `set_status_layanan()`: *Class method* untuk mengganti status operasional layanan logistik.
    *   `validasi_jenis_transaksi()`: *Static method* untuk memastikan jenis transaksi hanya bernilai "MASUK" atau "KELUAR".

> 📸 **Dokumentasi Output Class Arus Barang:**
> ![Screenshot Output Tes Arus Barang](https://github.com/arrosyidmahmuda/Praktikum-PBO/blob/f339f3ba5027b69b968638005c48b49aa4b36df3/posttest_1/Cuplikan%20layar%202026-09-23%20184957.png)
> 3. TES CLASS ARUS BARANG

---

### 3. Panduan Pengujian (Testing)
Pengujian program dilakukan secara otomatis saat menjalankan file `praktikum1.py`. Seluruh skenario pengujian telah ditanamkan (hardcoded) di dalam blok `if __name__ == "__main__":`.

**Cara Menjalankan:**
1. Buka terminal atau command prompt.
2. Navigasikan ke direktori tempat file `praktikum1.py` berada.
3. Jalankan perintah: `python praktikum1.py`
