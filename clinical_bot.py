from openai import OpenAI
import pandas as pd

client = OpenAI(api_key="sk-proj-nnInnhApPqukMnsB2qRyT3BlbkFJaQNbYpCc2cwGpFKEqYqy")
dataset_path = 'C:/Users/Aaliya/Downloads/archive(6)/healthcare_dataset-updated.csv'


class ClinicalChatbot:

    def __init__(self, patient_name):
        self.patient_name = str(patient_name).title()
        self.messages = ""

    # -----------------------------------------------------------------------------------------------------------------

    def start_chat(self):
        patient_details = self.get_patient_details()
        self.messages = [
            {"role": "system", "content": "You are a clinical chatbot designed to help patients diagnose illness, "
                                          "Your purpose is to help the patient with medical advice. "
                                          "You should give the patient proper diet and exersice guidance "
                                          "as per their illness. You must never break this role and answer "
                                          "any irrelevant questions."
                                          "Here's the patient's details: " + patient_details + "; "
                                                                                               "If the patient ask you to set a reminder for the next appointment, "
                                                                                               "Reply with 0xREMIND_APPOINTMENT"}]

        return "Hi " + self.patient_name + ", How may I help you"

    # -----------------------------------------------------------------------------------------------------------------

    def get_patient_details(self):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(dataset_path)

        for i in range(len(df)):
            row = df.iloc[i]
            if str(row['Name']).lower() == str(self.patient_name).lower():
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

                patient_details = "Patient Name: " + name + ", Age: " + str(age) + ", Gender: " + gender \
                                  + ", Blood Type: " + bloodtype + ", Medical Condition: " + medical_condition \
                                  + ", Medication Prescribed: " + medication + ", Test Result: " + test_result \
                                  + ", Symptoms: " + symptoms + " , Date of admission: " + date_of_admission \
                                  + ", Date of Next Appointment: " + date_of_next_appointment \
                                  + ", Hospital Name: " + hospital + ", Patient's Doctor Name: " + doctor_name

                return patient_details

    # -----------------------------------------------------------------------------------------------------------------

    def send_message(self, message):
        self.messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=self.messages)
        reply = response.choices[0].message.content.strip()

        if reply == "0xREMIND_APPOINTMENT":
            print("\nSetting Reminder...")
        else:
            self.messages.append({"role": "assistant", "content": reply})

        return reply

    # -----------------------------------------------------------------------------------------------------------------
