
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


    
def main():
    
    st.markdown("<h1 style='text-align: center; color: #2a2b2a;'>A SYMPTOM-BASED COVID-19 DETECTION SYSTEM</h1>", unsafe_allow_html=True)

#     st.title("A SYMPTOM-BASED COVID-19 DETECTION SYSTEM")

    st.image("covid19.jpg")

    st.write("""
    **This system is a machine learning model designed to detect COVID-19 infection based on the symptoms presented by a patient.**
   
    Note: This is a numerical-based prediction system. Kindly type your responses in numbers i.e. 1 = Yes, 0 = No.
    
    **Answer the following questions:**
    """)
    
    # getting the input data from the user

#     Breathing_Problem = st.text_input("Do you have problems with breathing?", placeholder="Enter 1 for Yes, 0 for No")
#     Fever = st.text_input("Any fever?", placeholder="Enter 1 for Yes, 0 for No")
#     Dry_Cough = st.text_input("How about dry cough?", placeholder="Enter 1 for Yes, 0 for No")
#     Sore_throat = st.text_input("Do you feel like you have a sore throat?", placeholder="Enter 1 for Yes, 0 for No")
#     HyperTension = st.text_input("Do you experience hypertension?", placeholder="Enter 1 for Yes, 0 for No")
#     Abroad_travel = st.text_input("Travelled abroad recently?", placeholder="Enter 1 for Yes, 0 for No")
#     Contact_with_COVID_Patient = st.text_input("Have you been in contact with a COVID patient?", placeholder="Enter 1 for Yes, 0 for No")
#     Attended_Large_Gathering = st.text_input("Did you recently attend a large gathering?", placeholder="Enter 1 for Yes, 0 for No")
#     Visited_Public_Exposed_Places = st.text_input("Have you recently visited any public exposed places?", placeholder="Enter 1 for Yes, 0 for No")
#     Family_working_in_Public_Exposed_Places = st.text_input("Do you have a relative working in public exposed places?", placeholder="Enter 1 for Yes, 0 for No")
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.beta_columns(10)
    
    with col1:
        Breathing_Problem = st.text_input("Do you have problems with breathing?", placeholder="Enter 1 for Yes, 0 for No")
    
    with col2:
        Fever = st.text_input("Any fever?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col3:
        Dry_Cough = st.text_input("How about dry cough?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col4:
        Sore_throat = st.text_input("Do you feel like you have a sore throat?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col5:
        HyperTension = st.text_input("Do you experience hypertension?", placeholder="Enter 1 for Yes, 0 for No")
       
    with col6:
        Abroad_travel = st.text_input("Travelled abroad recently?", placeholder="Enter 1 for Yes, 0 for No")
     
    with col7:
        Contact_with_COVID_Patient = st.text_input("Have you been in contact with a COVID patient?", placeholder="Enter 1 for Yes, 0 for No")

    with col8:
        Attended_Large_Gathering = st.text_input("Did you recently attend a large gathering?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col9:
        Visited_Public_Exposed_Places = st.text_input("Have you recently visited any public exposed places?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col10:
        Family_working_in_Public_Exposed_Places = st.text_input("Do you have a relative working in public exposed places?", placeholder="Enter 1 for Yes, 0 for No")
        

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
    

    
    
    
    
    
    
