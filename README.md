# PERTEMUAN 13
## Debugging, Tracing, Testing, dan Test Case Python di VS Code dan Pengumpulan melalui GitHub

---

## 1. Identitas

- **Nama:** Sekar Wahyuningrum
- **NIM:** 2225250095
- **Mata Kuliah:** Algoritma dan Pemrograman

---

## 2. Tujuan Repository

Repository ini dibuat untuk memenuhi tugas Pertemuan 13 pada mata kuliah Algoritma dan Pemrograman.

Tujuan pembuatan repository ini adalah:

1. Memahami konsep tracing pada program Python.
2. Mempelajari cara kerja perulangan dan fungsi dalam Python.
3. Mengidentifikasi dan memperbaiki kesalahan pada program.
4. Melakukan pengujian program menggunakan test case.
5. Memahami penggunaan breakpoint dalam proses debugging.
6. Menguji kebenaran hasil keluaran program.
7. Menggunakan Visual Studio Code untuk menulis dan menjalankan program Python.
8. Menggunakan Git dan GitHub untuk menyimpan serta mengumpulkan hasil pekerjaan.

---

## 3. Struktur Folder Repository

Berikut struktur folder dan berkas yang digunakan dalam repository ini.

```text
pertemuan-13-debugging-2225250095/
│
├── README.md
├── .gitignore
│
├── kasus/
│   ├── kasus_01_batas_kelulusan.py
│   ├── kasus_02_rata_rata.py
│   └── kasus_03_file_nilai.py
│
├── latihan/
│   ├── 01_trace_loop.py
│   ├── 02_trace_fungsi.py
│   ├── 03_test_case.py
│   └── 04_debug_breakpoint.py
│
└── praktik/
    └── praktik_4_debugging.py
```

### Fungsi Setiap Folder dan Berkas

**A. README.md**

Berisi identitas, tujuan repository, struktur folder, cara menjalankan program, hasil pengujian, kesimpulan, refleksi, dan sumber yang digunakan.

**B. .gitignore**

Digunakan untuk menentukan berkas atau folder yang tidak perlu dimasukkan ke repository GitHub, seperti cache Python dan virtual environment.

**C. Folder `kasus`**

Berisi tiga program studi kasus.

- `kasus_01_batas_kelulusan.py`: Menentukan status kelulusan berdasarkan nilai.
- `kasus_02_rata_rata.py`: Menghitung rata-rata dari sekumpulan nilai.
- `kasus_03_file_nilai.py`: Menyimpan dan membaca data nilai menggunakan file teks.

**D. Folder `latihan`**

Berisi empat program latihan.

- `01_trace_loop.py`: Mengamati proses perulangan dan perubahan nilai variabel.
- `02_trace_fungsi.py`: Memahami proses kerja fungsi untuk menghitung diskon.
- `03_test_case.py`: Menguji program menggunakan beberapa test case.
- `04_debug_breakpoint.py`: Mempelajari penggunaan breakpoint dalam debugging.

**E. Folder `praktik`**

Berisi program praktik debugging.

- `praktik_4_debugging.py`: Menghitung total dan rata-rata nilai siswa serta mengamati perubahan variabel selama perulangan.

---

## 4. Cara Menjalankan Program di VS Code

Berikut langkah-langkah menjalankan program Python.

1. Buka aplikasi Visual Studio Code.
2. Pilih menu **File → Open Folder**.
3. Buka folder `pertemuan-13-debugging-2225250095`.
4. Pastikan Python sudah terpasang di komputer.
5. Pilih salah satu file Python di folder `kasus`, `latihan`, atau `praktik`.
6. Klik tombol **Run Python File** di pojok kanan atas.
7. Amati hasil program pada bagian Terminal.

Program juga dapat dijalankan melalui terminal dengan perintah berikut:

```bash
python nama_file.py
```

Contoh menjalankan program praktik:

```bash
python praktik/praktik_4_debugging.py
```

Jika perintah `python` tidak berfungsi di Windows, coba gunakan:

```bash
py praktik/praktik_4_debugging.py
```

---

## 5. Hasil Pengujian Kasus

### 5.1 Kasus 1: Menentukan Batas Kelulusan

**Nama file:** `kasus_01_batas_kelulusan.py`

Program ini menggunakan fungsi `status_lulus(nilai)` untuk menentukan status kelulusan berdasarkan nilai yang dimasukkan.

Ketentuan program:
- Nilai lebih dari 60 dinyatakan lulus.
- Nilai 60 atau kurang dinyatakan tidak lulus.

Contoh pengujian:

| No. | Nilai | Hasil yang Diharapkan |
|---|---:|---|
| 1 | 75 | Lulus |
| 2 | 50 | Tidak lulus |
| 3 | 60 | Tidak lulus |

**Hasil pengujian:**

Program memberikan hasil sesuai dengan kondisi yang ditentukan. Nilai 75 dinyatakan lulus, sedangkan nilai 50 dan 60 dinyatakan tidak lulus.

### 5.2 Kasus 2: Menghitung Rata-rata

**Nama file:** `kasus_02_rata_rata.py`

Program ini digunakan untuk menghitung rata-rata dari sekumpulan data nilai.

Data yang digunakan:

```python
[80, 90, 70]
```

Perhitungan:

Rata-rata = (80 + 90 + 70) / 3

Rata-rata = 240 / 3

Rata-rata = 80

**Hasil pengujian:**

```text
80.0
```

Program berhasil menghitung rata-rata dari tiga nilai dengan hasil 80.0.

### 5.3 Kasus 3: Menyimpan dan Membaca File Nilai

**Nama file:** `kasus_03_file_nilai.py`

Program ini digunakan untuk menyimpan daftar nilai siswa ke dalam file teks, kemudian membaca kembali data yang telah disimpan.

Data yang digunakan:

```python
[80, 90, 75, 60]
```

Hasil keluaran yang diharapkan:

```text
80
90
75
60
```

**Hasil pengujian:**

Program dapat menuliskan nilai ke dalam file `nilai_siswa.txt` dan membaca kembali nilai tersebut. File teks dibuat secara otomatis ketika program dijalankan.

---

## 6. Hasil Latihan Tracing dan Debugging

### 6.1 Latihan 1: Tracing Perulangan

**Nama file:** `01_trace_loop.py`

Program ini digunakan untuk mengamati proses perulangan dan perubahan nilai variabel.

```python
for i in range(1, 6):
    print("Perulangan ke-", i)
```

Hasil keluaran:

```text
Perulangan ke- 1
Perulangan ke- 2
Perulangan ke- 3
Perulangan ke- 4
Perulangan ke- 5
```

**Kesimpulan:**

Perulangan berjalan sebanyak lima kali, mulai dari angka 1 sampai angka 5.

### 6.2 Latihan 2: Tracing Fungsi

**Nama file:** `02_trace_fungsi.py`

Program ini digunakan untuk menghitung harga setelah mendapatkan diskon.

```python
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon


print(hitung_diskon(200000, 10))
```

Hasil keluaran:

```text
180000.0
```

**Kesimpulan:**

Harga awal sebesar Rp200.000 mendapatkan diskon 10%, sehingga harga setelah diskon menjadi Rp180.000.

### 6.3 Latihan 3: Test Case

**Nama file:** `03_test_case.py`

Latihan ini bertujuan menguji program menggunakan beberapa data masukan untuk memeriksa apakah hasilnya sesuai dengan ketentuan yang ditetapkan.

Test case dapat berupa:
- Data normal.
- Data batas.
- Data yang tidak sesuai dengan ketentuan program.

Setiap test case perlu dibandingkan dengan hasil yang diharapkan agar kesalahan program dapat ditemukan.

### 6.4 Latihan 4: Debugging dengan Breakpoint

**Nama file:** `04_debug_breakpoint.py`

Latihan ini digunakan untuk mempelajari cara menghentikan sementara jalannya program pada baris tertentu menggunakan breakpoint.

Breakpoint membantu mengamati nilai variabel, urutan eksekusi, dan perubahan data selama program berjalan.

---

## 7. Hasil Praktik 4: Debugging

**Nama file:** `praktik_4_debugging.py`

Program praktik digunakan untuk menghitung total dan rata-rata nilai siswa.

Data nilai:

```python
nilai_siswa = [80, 90, 70, 60]
```

Program menghitung jumlah seluruh nilai, kemudian membagi total nilai dengan jumlah data untuk mendapatkan rata-rata.

Hasil keluaran:

```text
Daftar nilai: [80, 90, 70, 60]
Total nilai: 300
Rata-rata nilai: 75.0
```

### Proses Debugging

Langkah-langkah debugging yang dilakukan:

1. Membuka file `praktik_4_debugging.py` di VS Code.
2. Memasang breakpoint pada baris `total = total + n`.
3. Memulai debugging menggunakan tombol **F5**.
4. Mengamati perubahan variabel `total` pada setiap perulangan.
5. Memeriksa hasil perhitungan total dan rata-rata.
6. Memastikan hasil keluaran sesuai dengan perhitungan manual.

### Tabel Tracing

| Perulangan | Nilai (`n`) | Total Sebelumnya | Total Setelah Penjumlahan |
|---|---:|---:|---:|
| 1 | 80 | 0 | 80 |
| 2 | 90 | 80 | 170 |
| 3 | 70 | 170 | 240 |
| 4 | 60 | 240 | 300 |

**Kesimpulan:**

Berdasarkan proses tracing, total nilai berubah pada setiap perulangan hingga mencapai 300. Rata-rata dari empat nilai tersebut adalah 75.0. Breakpoint membantu mengamati proses perhitungan secara bertahap.

---

## 8. Kesimpulan Pengujian

Berdasarkan seluruh kegiatan yang dilakukan, tracing, testing, dan debugging memiliki peran penting dalam pengembangan program Python.

Tracing membantu memahami alur eksekusi dan perubahan nilai variabel. Testing membantu memeriksa apakah program menghasilkan keluaran yang sesuai dengan hasil yang diharapkan. Debugging membantu menemukan dan memperbaiki kesalahan melalui pemeriksaan proses program, termasuk menggunakan breakpoint.

Dari pengujian kasus dan praktik, program dapat digunakan untuk menentukan status kelulusan, menghitung rata-rata, menyimpan dan membaca data nilai, serta menghitung total dan rata-rata nilai siswa.

Dengan melakukan pengujian secara sistematis, kesalahan dapat ditemukan lebih mudah dan hasil program dapat diperiksa sebelum dikumpulkan.

---

## 9. Refleksi

Melalui kegiatan Pertemuan 13, saya belajar bahwa membuat program tidak hanya berfokus pada penulisan kode, tetapi juga pada proses pemeriksaan dan pengujian.

Saya memahami cara mengamati perulangan menggunakan tracing, memeriksa fungsi, menguji program dengan beberapa test case, serta menggunakan breakpoint untuk mengamati perubahan nilai variabel.

Saya juga mendapatkan pengalaman menggunakan VS Code untuk menjalankan program Python dan GitHub untuk menyimpan hasil pekerjaan. Kegiatan ini membantu meningkatkan pemahaman saya dalam menemukan kesalahan dan memastikan program berjalan sesuai tujuan.

---

## 10. Sumber yang Digunakan

1. Bahan Ajar Pertemuan 13, *Debugging, Tracing, Testing, dan Test Case Python di VS Code dan Pengumpulan melalui GitHub*. Program Studi S1 Pendidikan Matematika, FKIP, Universitas Sultan Ageng Tirtayasa, Tahun Akademik 2026/2027.

