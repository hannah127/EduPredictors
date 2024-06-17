import numpy as np
import pandas as pd
import streamlit as st 
from sklearn import preprocessing
import pickle
import re

df_filtered = pd.read_csv('data/dataset_dropout_filtered.csv')

model = pickle.load(open('model/student-dropout-academic-success-model.pk1', 'rb'))
#encoder_dict = pickle.load(open('encoder.pkl', 'rb')) 
cols=df_filtered.columns.drop("Target")
  
def main(): 
    st.title("Dropout Predictor")

    marital_status = st.selectbox("Marital Status", ["1 – single", "2 – married", "3 – widower", "4 – divorced", "5 – facto union", "6 – legally separated"])
    application_mode = st.selectbox("Application mode", [
        "1 - 1st phase - general contingent",
        "2 - Ordinance No. 612/93",
        "5 - 1st phase - special contingent (Azores Island)",
        "7 - Holders of other higher courses",
        "10 - Ordinance No. 854-B/99",
        "15 - International student (bachelor)",
        "16 - 1st phase - special contingent (Madeira Island)",
        "17 - 2nd phase - general contingent",
        "18 - 3rd phase - general contingent",
        "26 - Ordinance No. 533-A/99, item b2) (Different Plan)",
        "27 - Ordinance No. 533-A/99, item b3 (Other Institution)",
        "39 - Over 23 years old",
        "42 - Transfer",
        "43 - Change of course",
        "44 - Technological specialization diploma holders",
        "51 - Change of institution/course",
        "53 - Short cycle diploma holders",
        "57 - Change of institution/course (International)"
    ])
    application_order = st.selectbox("Application order", [str(i) for i in range(10)])  # Between 0 and 9
    attendance = st.selectbox("Daytime/evening attendance", ["1 – daytime", "0 - evening"])
    previous_qualification = st.selectbox("Previous qualification", [
        "1 - Secondary education",
        "2 - Higher education - bachelor's degree",
        "3 - Higher education - degree",
        "4 - Higher education - master's",
        "5 - Higher education - doctorate",
        "6 - Frequency of higher education",
        "9 - 12th year of schooling - not completed",
        "10 - 11th year of schooling - not completed",
        "12 - Other - 11th year of schooling",
        "14 - 10th year of schooling",
        "15 - 10th year of schooling - not completed",
        "19 - Basic education 3rd cycle (9th/10th/11th year) or equiv.",
        "38 - Basic education 2nd cycle (6th/7th/8th year) or equiv.",
        "39 - Technological specialization course",
        "40 - Higher education - degree (1st cycle)",
        "42 - Professional higher technical course",
        "43 - Higher education - master (2nd cycle)"
    ])
    mothers_qualification = st.selectbox("Mother's qualification", [
        "1 - Secondary Education - 12th Year of Schooling or Eq.",
        "2 - Higher Education - Bachelor's Degree",
        "3 - Higher Education - Degree",
        "4 - Higher Education - Master's",
        "5 - Higher Education - Doctorate",
        "6 - Frequency of Higher Education",
        "9 - 12th Year of Schooling - Not Completed",
        "10 - 11th Year of Schooling - Not Completed",
        "11 - 7th Year (Old)",
        "12 - Other - 11th Year of Schooling",
        "14 - 10th Year of Schooling",
        "18 - General commerce course",
        "19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
        "22 - Technical-professional course",
        "26 - 7th year of schooling",
        "27 - 2nd cycle of the general high school course",
        "29 - 9th Year of Schooling - Not Completed",
        "30 - 8th year of schooling",
        "34 - Unknown",
        "35 - Can't read or write",
        "36 - Can read without having a 4th year of schooling",
        "37 - Basic education 1st cycle (4th/5th year) or equiv.",
        "38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
        "39 - Technological specialization course",
        "40 - Higher education - degree (1st cycle)",
        "41 - Specialized higher studies course",
        "42 - Professional higher technical course",
        "43 - Higher Education - Master (2nd cycle)",
        "44 - Higher Education - Doctorate (3rd cycle)"
    ])
    admission_grade = st.slider("Admission grade", 0, 200)
    displaced = st.selectbox("Displaced", ["1 – yes", "0 – no"])
    debtor = st.selectbox("Debtor", ["1 – yes", "0 – no"])
    tuition_fees_up_to_date = st.selectbox("Tuition fees up to date", ["1 – yes", "0 – no"])
    gender = st.selectbox("Gender", ["1 – male", "0 – female"])
    scholarship_holder = st.selectbox("Scholarship holder", ["1 – yes", "0 – no"])
    age_at_enrollment = st.slider("Age at enrollment", 0, 100)
    curricular_units_1st_sem_enrolled = st.number_input("Curricular units 1st sem (enrolled)", 0)
    curricular_units_1st_sem_evaluations = st.number_input("Curricular units 1st sem (evaluations)", 0)
    curricular_units_1st_sem_approved = st.number_input("Curricular units 1st sem (approved)", 0)
    curricular_units_1st_sem_grade = st.slider("Curricular units 1st sem (grade)", 0, 20)
    curricular_units_2nd_sem_enrolled = st.number_input("Curricular units 2nd sem (enrolled)", 0)
    curricular_units_2nd_sem_evaluations = st.number_input("Curricular units 2nd sem (evaluations)", 0)
    curricular_units_2nd_sem_approved = st.number_input("Curricular units 2nd sem (approved)", 0)
    curricular_units_2nd_sem_grade = st.slider("Curricular units 2nd sem (grade)", 0, 20)
    gdp = st.slider("GDP", -5.00, 5.00)

    if st.button("Predict"): 
        data = {
            "Marital status": marital_status,
            "Application mode": application_mode,
            "Application order": application_order,
            "Daytime/evening attendance": attendance,
            "Previous qualification": previous_qualification,
            "Mother's qualification": mothers_qualification,
            "Admission grade": admission_grade,
            "Displaced": displaced,
            "Debtor": debtor,
            "Tuition fees up to date": tuition_fees_up_to_date,
            "Gender": gender,
            "Scholarship holder": scholarship_holder,
            "Age at enrollment": age_at_enrollment,
            "Curricular units 1st sem (enrolled)": curricular_units_1st_sem_enrolled,
            "Curricular units 1st sem (evaluations)": curricular_units_1st_sem_evaluations,
            "Curricular units 1st sem (approved)": curricular_units_1st_sem_approved,
            "Curricular units 1st sem (grade)": curricular_units_1st_sem_grade,
            "Curricular units 2nd sem (enrolled)": curricular_units_2nd_sem_enrolled,
            "Curricular units 2nd sem (evaluations)": curricular_units_2nd_sem_evaluations,
            "Curricular units 2nd sem (approved)": curricular_units_2nd_sem_approved,
            "Curricular units 2nd sem (grade)": curricular_units_2nd_sem_grade,
            "GDP": gdp,
        }

        # Function to extract numerical part
        def extract_number(value):
            if isinstance(value, str):
                match = re.match(r"\d+", value)
                return int(match.group()) if match else None
            elif isinstance(value, (int, float)):
                return value
            return None

        # Apply the function to each value in the dictionary
        mapped_data = {k: extract_number(v) for k, v in data.items()}

        #st.write(mapped_data)
        #print(mapped_data)
        df=pd.DataFrame([list(mapped_data.values())], columns=cols)
            
        features_list = df.values.tolist()      
        prediction = model.predict(features_list)
    
        output = int(prediction[0])
        if output == 1:
            text = "Graduate"
        else:
            text = "Dropout"

        st.success('You will {}'.format(text))

if __name__=='__main__': 
    main()