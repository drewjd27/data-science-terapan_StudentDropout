import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("rf_best_model.pkl")

st.title("Student's Status Prediction (Dropout, atau Graduate)")

# Mapping
marital_status_map = {"Single": 1, "Married": 2, "Widower": 3, "Divorced": 4, "Facto Union": 5, "Legally Separated": 6}
application_mode_map = {"1st phase - general contingent": 1, "Ordinance No. 612/93": 2, "1st phase - special contingent (Azores Island)": 5,
                        "Holders of other higher courses": 7, "Ordinance No. 854-B/99": 10, "International student (bachelor)": 15,
                        "1st phase - special contingent (Madeira Island)": 16, "2nd phase - general contingent": 17,
                        "3rd phase - general contingent": 18, "Over 23 years old": 39, "Transfer": 42, "Change of course": 43,
                        "Technological specialization diploma holders": 44, "Change of institution/course": 51,
                        "Short cycle diploma holders": 53, "Change of institution/course (International)": 57}
course_map = {"Informatics Engineering": 9119, "Nursing": 9500, "Management": 9147, "Social Service": 9238, "Basic Education": 9853}
qualification_map = {"Secondary education": 1, "Higher education - bachelor's": 2, "Higher education - degree": 3,
                     "Higher education - master's": 4, "Higher education - doctorate": 5, "Frequency of higher education": 6,
                     "Other": 12, "Basic education 3rd cycle": 19}
occupation_map = {"Student": 0, "Executives": 1, "Scientists": 2, "Technicians": 3, "Admin Staff": 4, "Service/Security": 5,
                  "Farmers": 6, "Industry/Construction": 7, "Machine Operators": 8, "Unskilled Workers": 9, "Other": 90}
nationality_map = {"Portuguese": 1, "German": 2, "Spanish": 6, "Brazilian": 41, "Other": 999}

with st.form("form_prediksi"):
    col1, col2 = st.columns(2)

    with col1:
        marital_status = st.selectbox("Marital Status", list(marital_status_map.keys()))
        application_mode = st.selectbox("Application Mode", list(application_mode_map.keys()))
        application_order = st.slider("Application Order", 0, 9, 0)
        course = st.selectbox("Course", list(course_map.keys()))
        day_time = st.radio("Attendance Time", ["Daytime", "Evening"])
        previous_qualification = st.selectbox("Previous Qualification", list(qualification_map.keys()))
        previous_grade = st.slider("Previous Qualification Grade", 0, 200, 150)
        age = st.number_input("Age at Enrollment", 17, 80, 18)
        nationality = st.selectbox("Nationality", list(nationality_map.keys()))
        admission_grade = st.slider("Admission Grade", 0, 200, 150)
        gender = st.radio("Gender", ["Male", "Female"])

    with col2:
        displaced = st.radio("Displaced?", ["No", "Yes"])
        special_needs = st.radio("Educational Special Needs?", ["No", "Yes"])
        debtor = st.radio("Debtor?", ["No", "Yes"])
        tuition_up_to_date = st.radio("Tuition Fees Up to Date?", ["No", "Yes"])
        scholarship = st.radio("Scholarship Holder?", ["No", "Yes"])
        international = st.radio("International Student?", ["No", "Yes"])
        mother_qual = st.selectbox("Mother's Qualification", list(qualification_map.keys()))
        father_qual = st.selectbox("Father's Qualification", list(qualification_map.keys()))
        mother_occ = st.selectbox("Mother's Occupation", list(occupation_map.keys()))
        father_occ = st.selectbox("Father's Occupation", list(occupation_map.keys()))

    st.markdown("### Academic Performance - Semester 1")
    col3, col4 = st.columns(2)
    with col3:
        sem1_credited = st.number_input("1st Sem - Credited", 0, 50, 0)
        sem1_enrolled = st.number_input("1st Sem - Enrolled", 0, 50, 0)
        sem1_evaluated = st.number_input("1st Sem - Evaluated", 0, 50, 0)
        sem1_approved = st.number_input("1st Sem - Approved", 0, 50, 0)
    with col4:
        sem1_grade = st.slider("1st Sem - Grade", 0.0, 20.0, 10.0)
        sem1_no_eval = st.number_input("1st Sem - No Evaluation", 0, 50, 0)

    st.markdown("### Academic Performance - Semester 2")
    col5, col6 = st.columns(2)
    with col5:
        sem2_credited = st.number_input("2nd Sem - Credited", 0, 50, 0)
        sem2_enrolled = st.number_input("2nd Sem - Enrolled", 0, 50, 0)
        sem2_evaluated = st.number_input("2nd Sem - Evaluated", 0, 50, 0)
    with col6:
        sem2_approved = st.number_input("2nd Sem - Approved", 0, 50, 0)
        sem2_grade = st.slider("2nd Sem - Grade", 0.0, 20.0, 10.0)
        sem2_no_eval = st.number_input("2nd Sem - No Evaluation", 0, 50, 0)

    st.markdown("### Ekonomi (Regional)")
    col7, col8 = st.columns(2)
    with col7:
        unemployment = st.slider("Unemployment Rate", 0.0, 100.0, 10.0)
    with col8:
        inflation = st.slider("Inflation Rate", 0.0, 50.0, 2.0)

    gdp = st.number_input("GDP (juta Euro)", 0.0, 100000.0, 50000.0)

    submitted = st.form_submit_button("Prediksi Status")

if submitted:
    input_data = pd.DataFrame([{
        "Marital status": marital_status_map[marital_status],
        "Application mode": application_mode_map[application_mode],
        "Application order": application_order,
        "Course": course_map[course],
        "Daytime/evening attendance\t": 1 if day_time == "Daytime" else 0,
        "Previous qualification": qualification_map[previous_qualification],
        "Previous qualification (grade)": previous_grade,
        "Nacionality": nationality_map[nationality],
        "Mother's qualification": qualification_map[mother_qual],
        "Father's qualification": qualification_map[father_qual],
        "Mother's occupation": occupation_map[mother_occ],
        "Father's occupation": occupation_map[father_occ],
        "Admission grade": admission_grade,
        "Displaced": 1 if displaced == "Yes" else 0,
        "Educational special needs": 1 if special_needs == "Yes" else 0,
        "Debtor": 1 if debtor == "Yes" else 0,
        "Tuition fees up to date": 1 if tuition_up_to_date == "Yes" else 0,
        "Gender": 1 if gender == "Male" else 0,
        "Scholarship holder": 1 if scholarship == "Yes" else 0,
        "Age at enrollment": age,
        "International": 1 if international == "Yes" else 0,
        "Curricular units 1st sem (credited)": sem1_credited,
        "Curricular units 1st sem (enrolled)": sem1_enrolled,
        "Curricular units 1st sem (evaluations)": sem1_evaluated,
        "Curricular units 1st sem (approved)": sem1_approved,
        "Curricular units 1st sem (grade)": sem1_grade,
        "Curricular units 1st sem (without evaluations)": sem1_no_eval,
        "Curricular units 2nd sem (credited)": sem2_credited,
        "Curricular units 2nd sem (enrolled)": sem2_enrolled,
        "Curricular units 2nd sem (evaluations)": sem2_evaluated,
        "Curricular units 2nd sem (approved)": sem2_approved,
        "Curricular units 2nd sem (grade)": sem2_grade,
        "Curricular units 2nd sem (without evaluations)": sem2_no_eval,
        "Unemployment rate": unemployment,
        "Inflation rate": inflation,
        "GDP": gdp
    }])

    prediction = model.predict(input_data)[0]

    proba = model.predict_proba(input_data)[0]
    label_map = {0: "Non Dropout", 1: "Dropout"}

    st.success(f"Predicted Student's Status: **{label_map[prediction]}**")

    st.markdown("### Prediction Probability")
    prob_df = pd.DataFrame({
        "Status": [label_map[i] for i in range(len(proba))],
        "Probability": proba
    })

    st.bar_chart(prob_df.set_index("Status"))

    label_map = {0: "Non Dropout", 1: "Dropout"}
    st.success(f"Predicted Student's Status: **{label_map[prediction]}**")
