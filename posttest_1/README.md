# Laporan Praktikum Pemrograman Berorientasi Objek
## SIGMA (Sistem Informasi Gudang, Manufaktur dan Arus Barang)

Dokumentasi ini berisi penjelasan struktur kelas, arsitektur program, dan panduan pengujian untuk program manajemen logistik SIGMA yang ditulis dalam file `praktikum1.py`[cite: 5].

---

### 1. Deskripsi Program
Program SIGMA adalah simulasi sistem informasi berbasis Pemrograman Berorientasi Objek (OOP) dengan Python[cite: 5]. Program ini mengelola data inventaris barang, target produksi manufaktur, dan pencatatan arus masuk/keluar barang di gudang[cite: 5]. Program ini telah menerapkan konsep OOP secara komprehensif, meliputi penggunaan *Instance Attribute*, *Class Attribute*, *Encapsulation* (melalui *Private Attribute* dan *Property/Setter*), serta implementasi *Instance Method*, *Class Method*, dan *Static Method*[cite: 5].

---

### 2. Struktur Class dan Arsitektur
Program ini terdiri dari tiga kelas utama yang saling berinteraksi[cite: 5]:

#### A. Class `Barang`[cite: 5]
Berfungsi sebagai cetak biru untuk entitas barang di gudang logistik[cite: 5].
*   **Atribut Kelas:** `nama_instansi` bernilai "SIGMA Logistics Center" dan `total_jenis_barang` untuk melacak jumlah variasi barang[cite: 5].
*   **Atribut Instance:** `kode_barang`, `nama_barang`, `harga`, dan atribut *private* `__stok`[cite: 5].
*   **Encapsulation:** Akses ke `__stok` diatur menggunakan `@property` dan `@stok.setter` yang memvalidasi agar input berupa integer dan tidak bernilai negatif[cite: 5].
*   **Method Utama:** 
    *   `tampilkan_detail()`: *Instance method* untuk mencetak rincian barang[cite: 5].
    *   `dari_dictionary()`: *Class method* yang bertindak sebagai *alternative constructor* untuk membuat instansiasi objek dari struktur data dictionary[cite: 5].
    *   `validasi_kode_barang()`: *Static method* untuk memverifikasi apakah kode barang diawali dengan "BRG-" dan memiliki panjang minimal 7 karakter[cite: 5].

> 📸 **Dokumentasi Output Class Barang:**
> ![Screenshot Output Tes Barang](https://github.com/arrosyidmahmuda/Praktikum-PBO/blob/6caf4136ffe0e17583c82bfa6b80eff81804347a/posttest_1/Cuplikan%20layar%202026-09-23%20184917.png)
> *1. TES CLASS BARANG*

#### B. Class `Manufaktur`[cite: 5]
Mewakili divisi yang menangani proses perakitan atau produksi barang[cite: 5].
*   **Atribut Kelas:** `nama_instansi` bernilai "SIGMA Manufacturing Division", `total_proses_manufaktur`, dan `standar_mutu` bernilai "ISO-9001"[cite: 5].
*   **Atribut Instance:** `id_produksi`, `produk_jadi` (menyimpan referensi objek `Barang`), dan atribut *private* `__target_produksi`[cite: 5].
*   **Encapsulation:** Nilai target divalidasi oleh `@target_produksi.setter` agar selalu bertipe integer dan bernilai di atas 0[cite: 5].
*   **Method Utama:**
    *   `proses_produksi()`: *Instance method* yang mengeksekusi produksi dan secara otomatis menambahkan hasilnya ke properti `stok` pada objek `Barang` terkait[cite: 5].
    *   `ubah_standar_mutu()`: *Class method* untuk memperbarui atribut kelas `standar_mutu`[cite: 5].
    *   `hitung_estimasi_waktu()`: *Static method* untuk mengkalkulasi waktu produksi berdasarkan jumlah unit dan kecepatan per jam[cite: 5].

> 📸 **Dokumentasi Output Class Manufaktur:**
> ![Screenshot Output Tes Manufaktur](https://github.com/arrosyidmahmuda/Praktikum-PBO/blob/65394cc41f07d7fbbb4a68b70f7e556421553149/posttest_1/Cuplikan%20layar%202026-09-23%20184943.png)
> *(Ganti teks di dalam kurung dengan path/link screenshot hasil output bagian "2. TES CLASS MANUFAKTUR")*

#### C. Class `ArusBarang`[cite: 5]
Mengatur dan mencatat lalu lintas barang, baik yang masuk ke maupun keluar dari gudang[cite: 5].
*   **Atribut Kelas:** `nama_instansi` bernilai "SIGMA Logistics & Distribution", `total_transaksi`, dan `status_layanan` bernilai "Aktif"[cite: 5].
*   **Atribut Instance:** `id_transaksi`, `barang` (menyimpan referensi objek `Barang`), `jenis_transaksi`, dan atribut *private* `__jumlah_barang`[cite: 5].
*   **Encapsulation:** Nilai kuantitas transaksi dijaga oleh `@jumlah_barang.setter` agar harus berupa angka positif[cite: 5].
*   **Method Utama:**
    *   `eksekusi_transaksi()`: *Instance method* yang memverifikasi kecukupan stok; akan menambah `stok` barang jika jenis transaksi "MASUK", dan mengurangi `stok` jika "KELUAR"[cite: 5].
    *   `set_status_layanan()`: *Class method* untuk mengganti status operasional layanan logistik[cite: 5].
    *   `validasi_jenis_transaksi()`: *Static method* untuk memastikan jenis transaksi hanya bernilai "MASUK" atau "KELUAR"[cite: 5].

> 📸 **Dokumentasi Output Class Arus Barang:**
> ![Screenshot Output Tes Arus Barang](path/to/gambar_tes_arus_barang.png)
> *(Ganti teks di dalam kurung dengan path/link screenshot hasil output bagian "3. TES CLASS ARUS BARANG")*

---

### 3. Panduan Pengujian (Testing)
Pengujian program dilakukan secara otomatis saat menjalankan file `praktikum1.py`[cite: 5]. Seluruh skenario pengujian telah ditanamkan (hardcoded) di dalam blok `if __name__ == "__main__":`[cite: 5].

**Cara Menjalankan:**
1. Buka terminal atau command prompt.
2. Navigasikan ke direktori tempat file `praktikum1.py` berada.
3. Jalankan perintah: `python praktikum1.py`

**Skenario yang Diuji[cite: 5]:**
*   **Validasi Masukan Salah:** Program akan mencetak pesan "[Ups, Gagal!]" jika pengujian memasukkan stok negatif (-5) atau string ("banyak")[cite: 5]. Validasi serupa juga menguji target produksi dengan nilai 0 dan jumlah transaksi minus (-10)[cite: 5].
*   **Pemanggilan Static & Class Method:** Memastikan validasi kode `BRG-001` memberikan hasil `True` dan `LPT-123` memberikan hasil `False`, serta mengubah standar mutu pabrik menjadi "ISO-9001:2026"[cite: 5].
*   **Interaksi Antar-Objek:** Memastikan bahwa pemanggilan `proses_produksi(20)` pada pabrik dan `eksekusi_transaksi()` berhasil memperbarui stok pada master data barang secara sinkron[cite: 5].

> 📸 **Dokumentasi Rangkuman Hasil Akhir:**
> ![Screenshot Output Rangkuman](https://github.com/arrosyidmahmuda/Praktikum-PBO/blob/f339f3ba5027b69b968638005c48b49aa4b36df3/posttest_1/Cuplikan%20layar%202026-09-23%20184957.png)
> *(Ganti teks di dalam kurung dengan path/link screenshot hasil terminal yang menunjukkan bagian "RANGKUMAN HASIL AKHIR")*
