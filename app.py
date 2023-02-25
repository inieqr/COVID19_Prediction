
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

    
def main():
    
    
    # giving a title
    st.title("A SYMPTOM-BASED COVID-19 DETECTION SYSTEM USING SVM")

    st.image("covid19.jpeg")

    st.write("""
    ## About
   The "SYMPTOM-BASED COVID-19 DETECTION SYSTEM USING SVM" is a machine learning model designed to detect COVID-19 infection based on the symptoms presented by a patient. The model uses Support Vector Machines (SVM) algorithm, which is a supervised learning technique that can analyze and classify data by identifying patterns and making predictions. The symptom-based COVID-19 detection system can take a set of symptoms and predict whether a patient is infected with COVID-19 or not. The model was trained using a dataset of symptoms and COVID-19 infection status from real-world patients. The model's accuracy was validated using various metrics such as sensitivity, specificity, and accuracy, and was found to be highly accurate in predicting COVID-19 infection based on symptoms. The system has the potential to assist healthcare professionals in the early identification and diagnosis of COVID-19 cases, which is critical for timely treatment and preventing the spread of the virus. Additionally, it can be used for screening individuals at high risk of COVID-19 infection, such as those with travel history or exposure to infected individuals, to facilitate early diagnosis and treatment.
    **Note: This is a numerical-based prediction system. Kindly type your responses in numbers i.e. 1 represents Yes and 0 represents No.** 
    """)
    
    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
      Breathing_Problem = st.text_input('Do you have problems with breathing?')
    with col2:
      Fever = st.text_input('Any fever?')
    with col3:
      Dry_Cough = st.text_input('How about dry cough?')
    with col4:
      Sore_throat = st.text_input('Do you feel like you have a sore throat?')
    with col5:
      HyperTension = st.text_input('Do you experience hypertension?')
    with col1:
      Abroad_travel = st.text_input('Travelled abroad recently?')
    with col2:
      Contact_with_COVID_Patient = st.text_input('Have you been in contact with a COVID patient?')
    with col3:
      Attended_Large_Gathering = st.text_input('Did you recently attend a large gathering?')
    with col4:
      Visited_Public_Exposed_Places = st.text_input('Have you recently visited any public exposed places?')
    with col5:
      Family_working_in_Public_Exposed_Places = st.text_input('Do you have a relative working in public exposed places?')
    

    

    # code for Prediction
    covid_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Find out your status'):
        covid_prediction = loaded_model.predict([[Breathing_Problem, Fever, Dry_Cough, Sore_throat, HyperTension, Abroad_travel, Contact_with_COVID_Patient, Attended_Large_Gathering, Visited_Public_Exposed_Places, Family_working_in_Public_Exposed_Places]])
        
        if (covid_prediction[0] == 0):
          covid_diagnosis = 'Your COVID-19 status came out negative! You are safe.'
        else:
          covid_diagnosis = 'Your COVID-19 status is positive! Visit the nearest hospital for a proper COVID check-up!'

      
    st.success(covid_diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    