import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediksi Risiko Mahasiswa Dropout",
    page_icon="🎓",
    layout="wide"
)

try:
    model = joblib.load('model_random_forest_terbaik.joblib')
except:
    model = joblib.load('model_random_forest_terbaik.joblib')

st.title("🎓 Aplikasi Prediksi Risiko Mahasiswa Dropout")
st.write("Aplikasi web interaktif berbasis *Machine Learning* (Random Forest) untuk mendeteksi potensi mahasiswa putus studi secara dini.")

st.sidebar.header("🔍 Panel Input Data Mahasiswa")
st.sidebar.markdown("Sesuaikan parameter di bawah ini untuk mensimulasikan data akademik mahasiswa:")

st.sidebar.subheader("📊 Performa Akademik")
curricular_2nd_approved = st.sidebar.slider("SKS Disetujui (Semester 2)", 0, 20, 5)
curricular_1st_approved = st.sidebar.slider("SKS Disetujui (Semester 1)", 0, 20, 5)
curricular_2nd_grade = st.sidebar.slider("Nilai Rata-rata (Semester 2)", 0.0, 20.0, 12.0)
curricular_1st_grade = st.sidebar.slider("Nilai Rata-rata (Semester 1)", 0.0, 20.0, 12.0)

st.sidebar.subheader("💰 Finansial & Demografi")
tuition_fees = st.sidebar.selectbox("Status Pembayaran SPP", options=[1, 0], format_func=lambda x: "Lunas (1)" if x == 1 else "Menunggak (0)")
debtor = st.sidebar.selectbox("Status Pemilik Utang/Debitur", options=[0, 1], format_func=lambda x: "Tidak (0)" if x == 0 else "Ya (1)")
scholarship = st.sidebar.selectbox("Penerima Beasiswa", options=[0, 1], format_func=lambda x: "Tidak (0)" if x == 1 else "Ya (1)")
age = st.sidebar.slider("Usia Saat Pendaftaran", 17, 70, 20)
gender = st.sidebar.selectbox("Jenis Kelamin", options=[0, 1], format_func=lambda x: "Perempuan (0)" if x == 0 else "Laki-laki (1)")

st.sidebar.subheader("🏫 Jalur Masuk & Akademik Asal")
admission_grade = st.sidebar.slider("Nilai Ujian Masuk (Admission Grade)", 0.0, 200.0, 120.0)
previous_grade = st.sidebar.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 122.0)
displaced = st.sidebar.selectbox("Mahasiswa Perantau/Displaced", options=[1, 0], format_func=lambda x: "Ya (1)" if x == 1 else "Tidak (0)")

input_data = {
    'Marital_status': [1],
    'Application_mode': [17],
    'Application_order': [1],
    'Course': [33],
    'Daytime_evening_attendance': [1],
    'Previous_qualification': [1],
    'Previous_qualification_grade': [previous_grade],
    'Nacionality': [1],
    'Mothers_qualification': [1],
    'Fathers_qualification': [1],
    'Mothers_occupation': [3],
    'Fathers_occupation': [3],
    'Admission_grade': [admission_grade],
    'Displaced': [displaced],
    'Educational_special_needs': [0],
    'Debtor': [debtor],
    'Tuition_fees_up_to_date': [tuition_fees],
    'Gender': [gender],
    'Scholarship_holder': [scholarship],
    'Age_at_enrollment': [age],
    'International': [0],
    'Curricular_units_1st_sem_credited': [0],
    'Curricular_units_1st_sem_enrolled': [6],
    'Curricular_units_1st_sem_evaluations': [6],
    'Curricular_units_1st_sem_approved': [curricular_1st_approved],
    'Curricular_units_1st_sem_grade': [curricular_1st_grade],
    'Curricular_units_1st_sem_without_evaluations': [0],
    'Curricular_units_2nd_sem_credited': [0],
    'Curricular_units_2nd_sem_enrolled': [6],
    'Curricular_units_2nd_sem_evaluations': [6],
    'Curricular_units_2nd_sem_approved': [curricular_2nd_approved],
    'Curricular_units_2nd_sem_grade': [curricular_2nd_grade],
    'Curricular_units_2nd_sem_without_evaluations': [0],
    'Unemployment_rate': [10.8],
    'Inflation_rate': [1.4],
    'GDP': [1.79]
}

df_input = pd.DataFrame(input_data)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🚀 Eksekusi Prediksi")
    st.write("Klik tombol di bawah untuk melihat hasil analisis risiko berdasarkan parameter di panel samping.")
    
    if st.button("Jalankan Prediksi Status Mahasiswa", type="primary", use_container_width=True):
        try:
            prediction = model.predict(df_input)
            status_map = {
                0: 'Dropout (Berisiko Tinggi Putus Studi)', 
                1: 'Enrolled (Aktif / Belum Lulus)', 
                2: 'Graduate (Lulus)'
            }
            result = status_map.get(prediction[0], "Tidak diketahui")
            
            st.markdown("---")
            st.subheader("🎯 Hasil Prediksi Model:")
            if "Dropout" in result:
                st.error(f"⚠️ **Peringatan:** {result}")
                st.info("Saran Intervensi: Pihak akademik disarankan memberikan konseling atau bantuan finansial/akademik dini.")
            elif "Enrolled" in result:
                st.warning(f"📌 **Status:** {result}")
            else:
                st.success(f"🎉 **Selamat:** {result}")
                
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses prediksi: {e}")

with col2:
    st.subheader("📋 Ringkasan Data Input (Tampilan Vertikal)")
    st.write("Daftar seluruh parameter (36 fitur) yang dimasukkan ke dalam model:")
    
    df_transposed = df_input.T
    df_transposed.columns = ["Nilai Input"]
    
    st.dataframe(df_transposed, use_container_width=True, height=350)