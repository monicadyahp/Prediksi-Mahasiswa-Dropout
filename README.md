# Proyek Akhir: Prediksi Mahasiswa Dropout (Student Dropout Prediction)

## Informasi Diri

- **Nama:** Monica Dyah Pudyowati
- **ID Dicoding:** monicadyp
- **Email:** monicadyah.md14@gmail.com

## 1. Domain Proyek (Business Understanding)

Tingkat putus studi (_dropout_) mahasiswa berdampak negatif terhadap reputasi institusi pendidikan dan stabilitas finansial. Proyek ini bertujuan untuk membangun sistem prediktif berbasis _machine learning_ yang mampu mendeteksi mahasiswa berisiko tinggi melakukan _dropout_ secara dini, sehingga pihak institusi dapat memberikan intervensi akademik maupun finansial secara proaktif.

## 2. Metodologi & Alur Proyek

- **Data Understanding & EDA:** Menganalisis distribusi data, korelasi fitur, serta mengecek nilai kosong (_missing value_).
- **Data Preprocessing:** Melakukan pemisahan fitur dan label, _Label Encoding_ pada target, pembagian data (_Train-Test Split_), serta normalisasi fitur menggunakan _StandardScaler_.
- **Modeling:** Menggunakan algoritma **Random Forest Classifier** yang dioptimasi menggunakan **GridSearchCV** untuk mencari kombinasi parameter terbaik (_hyperparameter tuning_).
- **Evaluation:** Menggunakan _Confusion Matrix_, _Classification Report_ (Accuracy, Precision, Recall, F1-Score), serta mengekstrak _Feature Importances_ untuk transparansi model.

## 3. Tautan Penting

- **Business Dashboard (Looker Studio):** [https://datastudio.google.com/reporting/b25da8bc-56e1-4e5a-9b0f-ec6f3881a018](https://datastudio.google.com/reporting/b25da8bc-56e1-4e5a-9b0f-ec6f3881a018)
- **Live Streamlit App (Deployment):** [https://prediksi-mahasiswa-dropout.streamlit.app/](https://prediksi-mahasiswa-dropout.streamlit.app/)

## 4. Struktur Direktori Berkas Submission

```text
submission/
├── model_random_forest_terbaik.joblib
├── notebook.ipynb
├── app.py
├── README.md
├── requirements.txt
├── monicadyp-dashboard.png
└── Student_Dropout_Risk_Monitoring_Dashboard.pdf
```
