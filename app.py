
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
    
    col1, col2 = st.columns(2)
    
    with col1:
        Breathing_Problem = st.text_input("Do you have problems with breathing?", placeholder="Enter 1 for Yes, 0 for No")
    
    with col1:
        Fever = st.text_input("Any fever?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col1:
        Dry_Cough = st.text_input("How about dry cough?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col1:
        Sore_throat = st.text_input("Do you feel like you have a sore throat?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col1:
        HyperTension = st.text_input("Do you experience hypertension?", placeholder="Enter 1 for Yes, 0 for No")
       
    with col1:
        Abroad_travel = st.text_input("Travelled abroad recently?", placeholder="Enter 1 for Yes, 0 for No")
     
    with col1:
        Contact_with_COVID_Patient = st.text_input("Have you been in contact with a COVID patient?", placeholder="Enter 1 for Yes, 0 for No")

    with col1:
        Attended_Large_Gathering = st.text_input("Did you recently attend a large gathering?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col1:
        Visited_Public_Exposed_Places = st.text_input("Have you recently visited any public exposed places?", placeholder="Enter 1 for Yes, 0 for No")
        
    with col1:
        Family_working_in_Public_Exposed_Places = st.text_input("Do you have a relative working in public exposed places?", placeholder="Enter 1 for Yes, 0 for No")
        

    # code for Prediction
    covid_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Find out your status'):
        covid_prediction = loaded_model.predict([[Breathing_Problem, Fever, Dry_Cough, Sore_throat, HyperTension, Abroad_travel, Contact_with_COVID_Patient, Attended_Large_Gathering, Visited_Public_Exposed_Places, Family_working_in_Public_Exposed_Places]])
        
        if (covid_prediction[0] == 0):
          covid_diagnosis = "Great news! Your COVID-19 test results have returned negative, which means you are in good health and safe from the virus."
        else:
          covid_diagnosis = "You have tested positive for COVID-19! Please proceed to the nearest hospital for a comprehensive COVID check-up."


      
    st.success(covid_diagnosis)
    
    if covid_diagnosis == "Great news! Your COVID-19 test results have returned negative, which means you are in good health and safe from the virus.":
            st.image("vac.png")
    elif covid_diagnosis == "You have tested positive for COVID-19! Please proceed to the nearest hospital for a comprehensive COVID check-up.":
            st.image("vac.png")

        
    

       
    
    
    
if __name__ == '__main__':
    main()
    

    
    
    
    
    
    
