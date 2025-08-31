# 🖼️ Aplikasi Filter Gambar di Domain Frekuensi

Aplikasi desktop sederhana untuk memvisualisasikan efek **filter gambar** (low-pass & high-pass) di **domain frekuensi** menggunakan **Fast Fourier Transform (FFT)**.  
Proyek ini dibuat sebagai **tugas akhir mata kuliah Pengolahan Sinyal Digital (PSD).**
---

## 📜 Deskripsi Proyek
Aplikasi ini memungkinkan pengguna untuk:
- Memuat gambar,
- Menerapkan filter **low-pass** (efek blur/penghalusan),
- Menerapkan filter **high-pass** (deteksi tepi/penajaman),
- Melihat hasil perbandingan secara langsung.  

Proses filtering dilakukan sepenuhnya di domain frekuensi menggunakan **FFT (Fast Fourier Transform)** dari NumPy.  
Antarmuka pengguna dibangun dengan **Tkinter**, sehingga aplikasi tetap **interaktif dan mudah digunakan.**

---

## ✨ Fitur Utama
- **Muat Gambar**: Mendukung format populer `.jpg`, `.png`, `.bmp`.  
- **Filter Low-Pass**: Menghaluskan gambar dengan menahan komponen frekuensi rendah.  
- **Filter High-Pass**: Mendeteksi tepian dengan menahan komponen frekuensi tinggi.  
- **Slider Interaktif**: Mengatur radius filter secara real-time untuk kontrol efek.  
- **Tampilan Berdampingan**: Bandingkan gambar asli dengan hasil filter secara langsung.  

---

## 🛠️ Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama.  
- **Tkinter**: Library GUI standar Python.  
- **OpenCV-Python**: Membaca & memproses data gambar.  
- **NumPy**: Operasi numerik & FFT.  
- **Pillow (PIL)**: Menampilkan gambar NumPy/OpenCV di Tkinter.  

---

## 🚀 Cara Instalasi & Menjalankan

### 1. Clone Repositori
```bash
git clone https://github.com/nama-user-anda/nama-repo-anda.git
cd nama-repo-anda
```

### 2. Instal Dependensi
```bash
pip install opencv-python numpy Pillow
```

### 3. Jalankan Aplikasi
```bash
python app_gui.py
```
