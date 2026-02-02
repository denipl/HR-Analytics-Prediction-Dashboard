import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Judul Dashboard
st.title("📊 HR Analytics & Prediction Dashboard")
st.write("Project ini dibuat untuk menganalisis faktor yang mempengaruhi kinerja dan retensi karyawan.")

# 2. Upload Data
uploaded_file = st.file_uploader("Upload File CSV Data Karyawan", type=["csv"])

if uploaded_file is not None:
    # Membaca data
    df = pd.read_csv(uploaded_file)
    
    # Tampilkan Data Mentah (Preview)
    st.subheader("1. Preview Data Karyawan")
    st.dataframe(df.head())

    # 3. Analisis Ringkas (Metrics)
    st.subheader("2. Ringkasan Operasional")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Karyawan", len(df))
    col2.metric("Rata-rata Umur", f"{df['Age'].mean():.0f} Tahun")
    # Asumsi ada kolom 'Attrition' (Yes/No)
    attrition_rate = (df['Attrition'].value_counts(normalize=True)['Yes'] * 100)
    col3.metric("Tingkat Resign (Attrition)", f"{attrition_rate:.1f}%")

    # 4. Visualisasi Data (Insight)
    st.subheader("3. Visualisasi Insight SDM")

    # Grafik 1: Distribusi Departemen
    st.write("**Sebaran Karyawan per Departemen**")
    fig_dept = px.bar(df, x='Department', color='Department', title="Jumlah Karyawan per Departemen")
    st.plotly_chart(fig_dept)

    # Grafik 2: Hubungan Gaji vs Lama Bekerja
    st.write("**Analisis Gaji vs Lama Bekerja (YearsAtCompany)**")
    # Pastikan nama kolom sesuai dataset Kaggle (MonthlyIncome, YearsAtCompany)
    fig_salary = px.scatter(df, x='YearsAtCompany', y='MonthlyIncome', color='Attrition', 
                            title="Apakah gaji rendah memicu karyawan keluar?")
    st.plotly_chart(fig_salary)

else:
    st.info("Silakan upload file CSV (Gunakan dataset IBM HR Analytics dari Kaggle).")