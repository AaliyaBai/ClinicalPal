from openai import OpenAI
import pandas as pd

client = OpenAI(api_key="sk-proj-M2Fp47jj4w2LUU8P6s3KT3BlbkFJ7OJt5Y7WLYgINa9fNYQD")
dataset_path = 'dataset/healthcare_dataset-updated.csv'

df = pd.read_csv(dataset_path)

patient_name = "Bobby JacksOn"

#patient_details = "Patient Name: " + patient_name + ", Age: " + patient_age + ", Gender: " \
                #+ patient_gender + ", Blood Type: " + patient_bloodtype + ", Medical Condition: " + patient_medical_condition \
                #+ ", Medication Prescribed: " + patient_medication + ", Test Result: " + patient_test_result \
               # + ", Symptoms: " + patient_symptoms + " , Date of admission: " + patient_date_of_admission \
               # + ", Date of Next Appointment: " + patient_date_of_next_appointment \
                #+ ", Hospital Name: " + patient_hospital + ", Patient's Doctor Name: " + patient_doctor_name

for i in range(len(df)):
    row = df.iloc[i]
    if str(row['Name']).lower() == str(patient_name).lower():
        name = row['Name']
        age = row['Age']
        gender = row['Gender']
        bloodtype = row['Blood Type']
        medical_condition = row['Medical Condition']
        date_of_admission = row['Date of Admission']
        doctor_name = row['Doctor']
        hospital = row['Hospital']
        medication = row['Medication']
        test_result = row['Test Results']
        symptoms = row['Symptoms']
        date_of_next_appointment = row['Next Appointment Date']
        print(row)

