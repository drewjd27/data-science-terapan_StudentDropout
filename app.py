import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

# Load model
@st.cache_resource
def load_model():
    with open("rf_best_model.pkl", "rb") as file:
        return joblib.load(file)

model = load_model()

# Aplikasi utama
st.title("🎓 Prediksi Status Mahasiswa")

st.markdown("Masukkan informasi mahasiswa untuk memprediksi `Target` (dropout, enrolled, graduate):")

# Input dari pengguna
def user_input():
    data = {
        "Marital status": st.selectbox("Marital status", [1, 2, 3, 4, 5, 6]),
        "Application mode": st.selectbox("Application mode", [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57]),
        "Application order": st.slider("Application order", 0, 9, 1),
        "Course": st.selectbox("Course", [33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991]),
        "Daytime/evening attendance\t": st.selectbox("Daytime/evening attendance", [0, 1]),
        "Previous qualification": st.selectbox("Previous qualification", [1,2,3,4,5,6,9,10,12,14,15,19,38,39,40,42,43]),
        "Previous qualification (grade)": st.slider("Previous qualification grade", 0.0, 200.0, 100.0),
        "Nacionality": st.selectbox("Nacionality", [1,2,6,11,13,14,17,21,22,24,25,26,32,41,62,100,101,103,105,108,109]),
        "Mother's qualification": st.number_input("Mother's qualification", 0, 44, 1),
        "Father's qualification": st.number_input("Father's qualification", 0, 44, 1),
        "Mother's occupation": st.number_input("Mother's occupation", 0, 194, 0),
        "Father's occupation": st.number_input("Father's occupation", 0, 195, 0),
        "Admission grade": st.slider("Admission grade", 0.0, 200.0, 100.0),
        "Displaced": st.selectbox("Displaced", [0, 1]),
        "Educational special needs": st.selectbox("Educational special needs", [0, 1]),
        "Debtor": st.selectbox("Debtor", [0, 1]),
        "Tuition fees up to date": st.selectbox("Tuition fees up to date", [0, 1]),
        "Gender": st.selectbox("Gender", [0, 1]),
        "Scholarship holder": st.selectbox("Scholarship holder", [0, 1]),
        "Age at enrollment": st.slider("Age at enrollment", 16, 70, 20),
        "International": st.selectbox("International", [0, 1]),
        "Curricular units 1st sem (credited)": st.slider("1st Sem Credited", 0, 20, 0),
        "Curricular units 1st sem (enrolled)": st.slider("1st Sem Enrolled", 0, 20, 0),
        "Curricular units 1st sem (evaluations)": st.slider("1st Sem Evaluations", 0, 20, 0),
        "Curricular units 1st sem (approved)": st.slider("1st Sem Approved", 0, 20, 0),
        "Curricular units 1st sem (grade)": st.slider("1st Sem Grade", 0.0, 20.0, 10.0),
        "Curricular units 1st sem (without evaluations)": st.slider("1st Sem Without Evaluations", 0, 20, 0),
        "Curricular units 2nd sem (credited)": st.slider("2nd Sem Credited", 0, 20, 0),
        "Curricular units 2nd sem (enrolled)": st.slider("2nd Sem Enrolled", 0, 20, 0),
        "Curricular units 2nd sem (evaluations)": st.slider("2nd Sem Evaluations", 0, 20, 0),
        "Curricular units 2nd sem (approved)": st.slider("2nd Sem Approved", 0, 20, 0),
        "Curricular units 2nd sem (grade)": st.slider("2nd Sem Grade", 0.0, 20.0, 10.0),
        "Curricular units 2nd sem (without evaluations)": st.slider("2nd Sem Without Evaluations", 0, 20, 0),
        "Unemployment rate": st.slider("Unemployment rate", 0.0, 20.0, 10.0),
        "Inflation rate": st.slider("Inflation rate", 0.0, 20.0, 2.5),
        "GDP": st.number_input("GDP", value=50000.0, step=1000.0),
    }
    return pd.DataFrame([data])

# Prediksi
input_df = user_input()

if st.button("Prediksi"):
    prediction = model.predict(input_df)[0]
    st.success(f"📊 Prediksi hasil mahasiswa: **{prediction}**")
