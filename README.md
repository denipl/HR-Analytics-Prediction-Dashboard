
<img width="1030" height="779" alt="Screenshot 2026-02-02 134933" src="https://github.com/user-attachments/assets/9aa0a1ac-b72e-4385-9ae0-77e7676168a0" />

# HR Analytics Prediction Dashboard 📊

Proyek ini bertujuan untuk menganalisis data karyawan dan membangun model prediktif untuk mengidentifikasi faktor-faktor yang menyebabkan karyawan meninggalkan perusahaan (*attrition*). Hasil analisis disajikan dalam bentuk dashboard interaktif untuk membantu departemen HR dalam pengambilan keputusan berbasis data.

## 🎯 Tujuan Proyek

* **Analisis Deskriptif:** Memahami profil demografis dan kepuasan kerja karyawan.
* **Prediksi Attrition:** Membangun model *Machine Learning* untuk memprediksi probabilitas karyawan akan berhenti atau tetap bertahan.
* **Wawasan Strategis:** Mengidentifikasi variabel kunci (seperti lembur, kepuasan lingkungan, atau gaji) yang paling memengaruhi retensi karyawan.

## 📊 Dataset

Dataset yang digunakan (`analisis_data.csv`) mencakup berbagai parameter karyawan, antara lain:

* **Demografi:** Umur, Jenis Kelamin, Pendidikan, Status Pernikahan.
* **Pekerjaan:** Departemen, Peran Pekerjaan, Tingkat Jabatan, Keterlibatan Kerja.
* **Kinerja & Kepuasan:** Kepuasan Lingkungan, Kepuasan Kerja, Penilaian Kinerja.
* **Finansial:** Pendapatan Bulanan, Persentase Kenaikan Gaji, Tingkat Harian/Jam.
* **Riwayat:** Total Tahun Bekerja, Lama di Perusahaan saat ini, Tahun sejak Promosi Terakhir.

## 🛠️ Teknologi yang Digunakan

* **Python:** Bahasa pemrograman utama untuk analisis dan permodelan.
* **Pandas & NumPy:** Manipulasi dan pembersihan data.
* **Scikit-Learn:** Pembangunan model *Machine Learning* (Klasifikasi).
* **Plotly / Seaborn / Matplotlib:** Visualisasi data untuk dashboard.
* **Streamlit / Dash:** (Opsional) Kerangka kerja untuk dashboard web interaktif.

## 📂 Struktur Proyek

* `analisis_data.csv`: Dataset utama yang berisi informasi karyawan.
* `tes.py`: Skrip pengujian atau logika utama aplikasi.
* `README.md`: Dokumentasi proyek.

## 🚀 Cara Menjalankan

1. **Clone Repositori:**
```bash
git clone https://github.com/username-anda/hr-analytics-prediction-dashboard.git
cd hr-analytics-prediction-dashboard

```


2. **Instalasi Library:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn plotly streamlit

```


3. **Jalankan Dashboard:**
```bash
streamlit run tes.py

```



## 📈 Pratinjau Analisis

Dashboard ini mencakup visualisasi untuk:

* Distribusi Attrition berdasarkan departemen.
* Korelasi antara lembur (*OverTime*) dengan tingkat keluarnya karyawan.
* Pengaruh kepuasan kerja terhadap retensi.
