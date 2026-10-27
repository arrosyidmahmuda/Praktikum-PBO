# SIGMA Logistics & Manufacturing System

Program Python berbasis OOP yang mensimulasikan alur **logistik dan manufaktur** pada SIGMA Logistics Center: barang (elektronik dan pakaian) diproduksi oleh divisi manufaktur, bahan bakunya dikirim oleh supplier, lalu barang keluar-masuk gudang lewat transaksi distribusi.

Cara menjalankan:

```bash
python main.py
```

---

## 1. Class Diagram

![Class Diagram](/assets/Class_diagram.png)

| Simbol | Arti |
|---|---|
| Panah terbuka (`──>`) | Asosiasi |
| Belah ketupat **kosong** (`◇──`) | Agregasi |
| Belah ketupat **hitam** (`◆──`) | Komposisi |
| Segitiga kosong (`──▷`) | Pewarisan |

### Penjelasan Relasi

**Asosiasi: `Supplier` → `Manufaktur`**
`Supplier` hanya menggunakan `Manufaktur` sebagai parameter pada method `kirim_bahan_baku(manufaktur)`, tanpa menyimpannya sebagai atribut. Hubungannya longgar: supplier cukup tahu manufaktur mana yang dikirimi bahan baku.

**Agregasi: `Manufaktur` ◇→ `Barang` dan `ArusBarang` ◇→ `Barang`**
Objek `Barang` dibuat di luar (di `main`), lalu dimasukkan lewat constructor (`produk_jadi` pada `Manufaktur`, `barang` pada `ArusBarang`). Ini agregasi, bukan komposisi, karena `Barang` hidup mandiri: objek `barang_elektronik` dipakai bersama oleh `Manufaktur` dan `ArusBarang`, dan tetap ada walaupun salah satunya dihapus.

**Komposisi: `Manufaktur` ◆→ `MesinProduksi`**
`MesinProduksi` dibuat langsung di dalam constructor `Manufaktur` (`self.mesin_lini = MesinProduksi(f"Robot-Assembly-{self.id_produksi}")`). Ini komposisi karena mesin itu bagian dari satu lini produksi saja, namanya mengikuti `id_produksi`, tidak dibuat atau dipakai di luar `Manufaktur`, dan siklus hidupnya mengikuti pemiliknya. Jika `Manufaktur` dihapus, mesinnya ikut hilang.

---

## 2. Abstraksi

| Ketentuan | Penerapan di kode |
|---|---|
| Abstract class (ABC) | `Barang(ABC)` |
| Minimal 2 `@abstractmethod` | `tampilkan_detail()` dan `hitung_biaya_simpan()` |
| Minimal 2 subclass mengimplementasikan semuanya | `BarangElektronik` dan `BarangPakaian` |
| Method konkret yang dipakai bersama | `hitung_nilai_stok()` dan `cetak_laporan()` (method template, mirip `jalankan()` di materi: memanggil abstract method milik tiap subclass) |
| Bukti tidak bisa diinstansiasi | `try: Barang(...) except TypeError` pada bagian *4. BUKTI ABSTRAKSI* di `main` |

Konsep inheritance dari posttest sebelumnya tetap dipakai:

- `super().__init__(...)` di `BarangElektronik` dan `BarangPakaian`.
- Atribut unik tiap subclass: `daya_watt` (elektronik), `ukuran` dan `_bahan` (pakaian).
- Atribut **protected** `_harga`, `_bahan` dan atribut **private** `__stok`, `__target_produksi`, `__jumlah_barang`.

---

## 3. Polimorfisme

**Polimorfisme via pewarisan.**
`tampilkan_detail()` dan `hitung_biaya_simpan()` di-override oleh `BarangElektronik` dan `BarangPakaian` dengan perilaku berbeda (elektronik: 1% dari nilai stok; pakaian: Rp2.000 per unit). Keduanya dipanggil lewat satu loop `for barang in daftar_barang: barang.cetak_laporan()` (bagian *5. POLIMORFISME VIA PEWARISAN*).

**Duck typing.**
`Manufaktur` dan `ArusBarang` tidak berhubungan lewat pewarisan, tetapi sama-sama punya method `cetak_status()`. Keduanya dipanggil lewat satu fungsi, `tampilkan_status(objek)` (bagian *6. DUCK TYPING*).

**Operator overloading.**
Pada kelas `Barang`: `__str__` (teks `kode - nama`), `__lt__` (membandingkan harga, sehingga objek bisa di-`sorted()`), dan `__add__` (menjumlahkan nilai stok dua barang). Bagian *7. OPERATOR OVERLOADING*.

Bagian polimorfisme di atas tidak memakai rantai `if/elif` yang mengecek `type()` atau string jenis; setiap objek menentukan perilakunya sendiri lewat method.

---

## 4. Screenshot Output Program

![Output Program](/assets/output1.png)
![Output Program](/assets/output2.png)

Bukti abstract class tidak bisa diinstansiasi ada pada bagian **4. BUKTI ABSTRAKSI**:

```
TypeError: Can't instantiate abstract class Barang without an implementation for abstract methods 'hitung_biaya_simpan', 'tampilkan_detail'
```

---

## 5. Penerapan SOLID

**Open/Closed Principle (OCP)**
Menambah jenis barang baru (misalnya `BarangMakanan`) cukup dengan membuat subclass dari `Barang` dan mengimplementasikan dua abstract method-nya. Loop `cetak_laporan()`, `sorted()`, operator `+`, `ArusBarang`, dan `Manufaktur` tidak perlu diubah, karena semuanya hanya memanggil method yang dijamin oleh `Barang`.

**Dependency Inversion Principle (DIP)**
`ArusBarang` dan `Manufaktur` menerima objek barang lewat constructor (*dependency injection*) dan bergantung pada abstraksi `Barang`, bukan pada `BarangElektronik` atau `BarangPakaian` secara langsung. Karena itu keduanya bisa dipakai untuk jenis barang apa pun.
