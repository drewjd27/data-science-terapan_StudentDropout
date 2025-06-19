# Proyek Akhir: Menyelesaikan Permasalahan Dropout Perusahaan Edutech Jaya Jaya Institut

## Business Understanding

Perusahaan edutech Jaya Jaya Institut menghadapi tantangan dalam mempertahankan mahasiswa untuk menyelesaikan program pendidikan mereka. Tingkat dropout yang tinggi tidak hanya berdampak pada reputasi institusi pendidikan, tetapi juga mengurangi revenue dan efisiensi operasional. Dengan total 4,424 mahasiswa dan tingkat dropout mencapai 1,421 mahasiswa (sekitar 32.1%), perusahaan membutuhkan solusi berbasis data untuk mengidentifikasi faktor-faktor yang mempengaruhi dropout dan melakukan intervensi dini.

### Permasalahan Bisnis

1. **Tingkat Dropout Tinggi**: Dari 4,424 total mahasiswa, 1,421 mahasiswa (32.1%) mengalami dropout, yang menunjukkan masalah serius dalam retensi mahasiswa.

2. **Kurangnya Prediksi Dini**: Perusahaan tidak memiliki sistem untuk memprediksi mahasiswa yang berisiko dropout sehingga sulit melakukan intervensi preventif.

3. **Pemahaman Faktor Risiko Terbatas**: Tidak ada analisis mendalam tentang faktor-faktor yang berkontribusi terhadap dropout, seperti status beasiswa, status pernikahan, jadwal kuliah, dan program studi.

4. **Ketidakefisienan Sumber Daya**: Tanpa prediksi yang akurat, alokasi sumber daya untuk program retensi mahasiswa menjadi tidak efektif.

### Cakupan Proyek

1. **Analisis Data Eksploratif**: Menganalisis pola dropout berdasarkan berbagai faktor demografis dan akademis mahasiswa.

2. **Pengembangan Model Prediksi**: Membangun dan membandingkan model machine learning (Random Forest vs XGBoost) untuk memprediksi dropout.

3. **Business Dashboard**: Membuat dashboard interaktif untuk visualisasi insight dan monitoring tingkat dropout.

4. **Prototype Aplikasi**: Mengembangkan aplikasi web berbasis Streamlit untuk prediksi dropout real-time.

5. **Rekomendasi Strategis**: Memberikan action items berdasarkan temuan analisis data.

### Persiapan

**Sumber data**: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

**Setup environment**:
```bash
# clone repository
git clone https://github.com/drewjd27/data-science-terapan_StudentDropout.git
cd data-science-terapan_StudentDropout

# buat virtual environment
python3 -m venv student_dropout
source student_dropout/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Business Dashboard

Dashboard telah dikembangkan menggunakan Looker Studio untuk memberikan insight visual yang komprehensif tentang pola dropout mahasiswa. Pada looker studio, ditambahkan field baru bernama `Dropout Count` agar dapat melihat jumlah mahasiswa dropout dengan formula berikut ini.


```
CASE
  WHEN Target = "Dropout" THEN 1
  ELSE 0
END
```


| ![drewjd27-dashboard](https://github.com/user-attachments/assets/68e74422-f5f0-4c6f-8db8-a8ac0b798689) |
|:--:| 
| *Dashboard yang Dibangun di Looker Studio* |

Dashboard menampilkan:

- **Overview Dropout**: Total mahasiswa, target berdasarkan status, dan jumlah dropout
- **Analisis Demografis**: Distribusi dropout berdasarkan gender, status pernikahan
- **Faktor Sosial Ekonomi**: Impact status beasiswa dan debt terhadap dropout
- **Faktor Akademis**: Pola dropout berdasarkan program studi dan jadwal kuliah (siang/malam)
- **Status Displacement**: Analisis mahasiswa yang pindah vs dropout

### Temuan Utama dari Dashboard:

1. **Distribusi Target**: 
   - 49.9% siswa berhasil Graduate
   - 32.1% siswa Dropout
   - 17.9% siswa masih Enrolled

2. **Faktor Beasiswa**: 
   - 90.6% siswa dropout tidak memiliki beasiswa
   - Hanya 9.4% siswa dropout yang memiliki beasiswa
   - Menunjukkan korelasi kuat antara dukungan finansial dan tingkat dropout

3. **Status Displacement**:
   - 52.9% siswa dropout tidak mengalami displacement
   - 47.1% mengalami displacement
   - Faktor geografis dan mobilitas berpengaruh terhadap dropout

4. **Distribusi Gender**:
   - Relatif seimbang antara male (50.7%) dan female (49.3%) dalam kasus dropout

5. **Status Debitur**:
   - 78% siswa dropout tidak memiliki status sebagai debitur
   - 22% adalah debitur, menunjukkan masalah finansial

6. **Pola Kehadiran**:
   - 85.4% siswa dropout mengikuti program daytime
   - 14.6% mengikuti program evening

7. **Status Pernikahan**:
   - Mayoritas siswa dropout berstatus single (sekitar 1,100+ siswa)
   - Diikuti oleh married, divorced, dan status lainnya dengan jumlah jauh lebih sedikit

8. **Program Studi dengan Dropout Tertinggi**:
   - Management (evening attendance): ~130 siswa
   - Management: ~125 siswa
   - Nursing: ~115 siswa
   - Journalism and Communication: ~105 siswa

**Link Dashboard**: https://lookerstudio.google.com/u/0/reporting/e331a1ea-fceb-404c-a4dc-ebf0aded3458/page/cUaOF

## Menjalankan Sistem Machine Learning

Prototype sistem machine learning telah dikembangkan menggunakan Streamlit dengan model XGBoost yang telah dioptimasi. Sistem ini memungkinkan prediksi dropout berdasarkan input karakteristik mahasiswa.

**Cara menjalankan locally**:
```bash
git clone https://github.com/drewjd27/data-science-terapan_StudentDropout.git
cd data-science-terapan_StudentDropout
pip install -r requirements.txt
streamlit run app.py
```

**Akses Aplikasi Secara Online**: https://student-status-drewjd27.streamlit.app/


## Conclusion

Proyek ini berhasil mengidentifikasi faktor-faktor kunci yang mempengaruhi dropout mahasiswa dan mengembangkan sistem prediksi dengan akurasi tinggi menggunakan model XGBoost. Analisis menunjukkan bahwa:

1. **Model XGBoost** memberikan performa terbaik dibandingkan Random Forest untuk kasus prediksi dropout. Akurasi XGBoost 88.47%, akurasi Random Forest 88.36%.
2. **Faktor demografis** seperti status pernikahan (mayoritas dropout adalah mahasiswa single) dan gender memiliki pengaruh signifikan
3. **Status beasiswa** menunjukkan bahwa 90.6% mahasiswa dropout tidak memiliki beasiswa
4. **Jadwal kuliah** mempengaruhi dropout dengan 85.4% mahasiswa dropout mengikuti kelas siang hari
5. **Program studi** tertentu seperti Management dan Nursing memiliki tingkat dropout tertinggi

### Rekomendasi Action Items

- **Program Beasiswa Terpadu**: Perluas program beasiswa khususnya untuk mahasiswa dari latar belakang ekonomi kurang mampu, mengingat 90.6% dropout tidak memiliki beasiswa

- **Early Warning System**: Implementasikan sistem prediksi dropout berbasis machine learning untuk identifikasi dini mahasiswa berisiko tinggi

- **Program Mentoring Khusus**: Fokuskan program mentoring pada mahasiswa single, program studi Management dan Nursing, serta mahasiswa kelas siang yang menunjukkan risiko dropout tertinggi

- **Flexible Learning Options**: Kembangkan program pembelajaran fleksibel untuk mahasiswa yang bekerja atau memiliki keterbatasan waktu, terutama yang mengikuti kelas siang

- **Financial Counseling**: Sediakan layanan konseling keuangan dan program cicilan yang terjangkau untuk mengurangi tekanan finansial mahasiswa

- **Academic Support Program**: Intensifkan program bimbingan akademik untuk program studi dengan tingkat dropout tinggi dengan pendekatan yang disesuaikan per program studi

- **Regular Monitoring Dashboard**: Gunakan business dashboard secara rutin untuk monitoring trend dropout dan evaluasi efektivitas program retensi mahasiswa
