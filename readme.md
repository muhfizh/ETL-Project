# ETL Project

## Deskripsi

Proyek ini merupakan implementasi pipeline ETL (Extract, Transform, Load) menggunakan Python. Pipeline ini bertujuan untuk mengekstrak data dari file CSV, melakukan transformasi sederhana, dan memuat hasilnya ke dalam file output yang telah dibersihkan.

## Fitur

- Ekstraksi data dari file CSV
- Transformasi data (pembersihan data kosong, konversi format)
- Pemuatan data ke file hasil akhir
- Struktur modular: kode dibagi menjadi beberapa modul (extract, transform, load)

## Struktur Direktori

```
ETL-Project/
├── config/
│   └── config.yaml           # Konfigurasi ETL
├── data/
│   ├── penjualan.csv         # File csv
│   ├── penjualan.excel       # File excel
├── etl/
│   ├── extract.py            # Modul ekstraksi data
│   ├── transform.py          # Modul transformasi data
│   └── load.py               # Modul pemuatan data
├── main.py                   # Script utama untuk menjalankan ETL
├── requirements.txt          # Dependensi proyek
└── README.md                 # Dokumentasi proyek
```

## Cara Menjalankan

1. **Clone repositori ini**

```bash
git clone https://github.com/muhfizh/ETL-Project.git
cd ETL-Project
```

2. **Buat environment dan install dependensi**

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

3. **Siapkan file input di folder `data/input/`**

4. **Jalankan pipeline ETL**

```bash
python main.py
```

Hasil akhir akan masuk ke database.

---

© 2025 [muhfizh](https://github.com/muhfizh)
