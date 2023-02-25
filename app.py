
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def reset():
    if st.button("Reset"):
        st.experimental_rerun()

    
def main():
    
    
    # giving a title
    st.title("A SYMPTOM-BASED COVID-19 DETECTION SYSTEM USING SVM")

    st.image("covid19.jpg")

    st.write("""
    ## About
   This system is a machine learning model designed to detect COVID-19 infection based on the symptoms presented by a patient.
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
    
       # Call the reset function anywhere in your app
    reset()
    
    
    
    
    
    
    
