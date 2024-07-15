from openai import OpenAI

client = OpenAI(api_key="sk-proj-nnInnhApPqukMnsB2qRyT3BlbkFJaQNbYpCc2cwGpFKEqYqy")

patient_name = "Aaliya"
patient_age = "28"
patient_gender = "Female"
patient_bloodtype = "O+"
patient_medical_condition = "Fever"
patient_date_of_admission = "01-07-2024"
patient_doctor_name = "Gopi Krishnan"
patient_hospital = "Aster Medicity"
patient_medication = "Penicillin"
patient_test_result = "Abnormal"
patient_symptoms = "High temperature, Sweating, Shivering"
patient_date_of_next_appointment = "15-07-2024"

patient_details = "Patient Name: " + patient_name + ", Age: " + patient_age + ", Gender: " \
                + patient_gender + ", Blood Type: " + patient_bloodtype + ", Medical Condition: " + patient_medical_condition \
                + ", Medication Prescribed: " + patient_medication + ", Test Result: " + patient_test_result \
                + ", Symptoms: " + patient_symptoms + " , Date of admission: " + patient_date_of_admission \
                + ", Date of Next Appointment: " + patient_date_of_next_appointment \
                + ", Hospital Name: " + patient_hospital + ", Patient's Doctor Name: " + patient_doctor_name

messages = [{"role": "system", "content": "You are a clinical chatbot designed to help patients diagnose illness, "
                                          "Your purpose is to help the patient with medical advice. "
                                          "You should give the patient proper diet and exersice guidance "
                                          "as per their illness. You must never break this role and answer "
                                          "any irrelevant questions."
                                          "Here's the patient's details: " + patient_details + "; "
                                          "If the patient ask you to set a reminder for the next appointment, "
                                          "Reply with 0xREMIND_APPOINTMENT"}]

print("Hi " + patient_name + ", How may I help you")

while True:
    message = input()

    if message == 'quit()':
        break

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    reply = response.choices[0].message.content.strip()

    if reply == "0xREMIND_APPOINTMENT":
        print("\nSetting Reminder...")
    else:
        messages.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")

