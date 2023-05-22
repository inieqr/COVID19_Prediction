
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

#     Breathing_Problem = st.text_input("Difficulty in Breathing", placeholder="Enter 1 for Yes, 0 for No")
#     Fever = st.text_input("Fever", placeholder="Enter 1 for Yes, 0 for No")
#     Dry_Cough = st.text_input("Dry Cough", placeholder="Enter 1 for Yes, 0 for No")
#     Sore_throat = st.text_input("Sore Throat", placeholder="Enter 1 for Yes, 0 for No")
#     HyperTension = st.text_input("HyperTension", placeholder="Enter 1 for Yes, 0 for No")
#     Abroad_travel = st.text_input("Abroad Travel", placeholder="Enter 1 for Yes, 0 for No")
#     Contact_with_COVID_Patient = st.text_input("Contact With A Patient", placeholder="Enter 1 for Yes, 0 for No")
#     Attended_Large_Gathering = st.text_input("Attended Large Gathering", placeholder="Enter 1 for Yes, 0 for No")
#     Visited_Public_Exposed_Places = st.text_input("Visited Public Exposed Places", placeholder="Enter 1 for Yes, 0 for No")
#     Family_working_in_Public_Exposed_Places = st.text_input("Family working in Public Exposed Places", placeholder="Enter 1 for Yes, 0 for No")

    
    def text_field(label, columns=None, **input_params):
        c1, c2 = st.beta_columns(columns or [1, 4])

        # Display field name with some alignment
        c1.markdown("##")
        c1.markdown(label)

        # Sets a default key parameter to avoid duplicate key errors
        input_params.setdefault("key", label)

        # Forward text input parameters
        return c2.text_input("", **input_params)


    Breathing_Problem = text_field("Difficulty in Breathing", placeholder="Enter 1 for Yes, 0 for No")
    Fever = text_field("Fever", placeholder="Enter 1 for Yes, 0 for No")
    Dry_Cough = text_field("Dry Cough", placeholder="Enter 1 for Yes, 0 for No")
    Sore_throat = text_field("Sore Throat", placeholder="Enter 1 for Yes, 0 for No")
    HyperTension = text_field("HyperTension", placeholder="Enter 1 for Yes, 0 for No")
    Abroad_travel = text_field("Abroad Travel", placeholder="Enter 1 for Yes, 0 for No")
    Contact_with_COVID_Patient = text_field("Contact With A Patient", placeholder="Enter 1 for Yes, 0 for No")
    Attended_Large_Gathering = text_field("Attended Large Gathering", placeholder="Enter 1 for Yes, 0 for No")
    Visited_Public_Exposed_Places = text_field("Visited Public Exposed Places", placeholder="Enter 1 for Yes, 0 for No")
    Family_working_in_Public_Exposed_Places = text_field("Family working in Public Exposed Places", placeholder="Enter 1 for Yes, 0 for No")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         Breathing_Problem = st.text_input("Difficulty in Breathing", placeholder="Enter 1 for Yes, 0 for No")
    
#     with col1:
#         Fever = st.text_input("Fever", placeholder="Enter 1 for Yes, 0 for No")
        
#     with col1:
#         Dry_Cough = st.text_input("Dry Cough", placeholder="Enter 1 for Yes, 0 for No")
        
#     with col1:
#         Sore_throat = st.text_input("Sore Throat", placeholder="Enter 1 for Yes, 0 for No")
        
#     with col1:
#         HyperTension = st.text_input("HyperTension", placeholder="Enter 1 for Yes, 0 for No")
       
#     with col1:
#         Abroad_travel = st.text_input("Abroad Travel", placeholder="Enter 1 for Yes, 0 for No")
     
#     with col1:
#         Contact_with_COVID_Patient = st.text_input("Contact With A Patient", placeholder="Enter 1 for Yes, 0 for No")

#     with col1:
#         Attended_Large_Gathering = st.text_input("Attended Large Gathering", placeholder="Enter 1 for Yes, 0 for No")
        
#     with col1:
#         Visited_Public_Exposed_Places = st.text_input("Visited Public Exposed Places", placeholder="Enter 1 for Yes, 0 for No")
        
#     with col1:
#         Family_working_in_Public_Exposed_Places = st.text_input("Family working in Public Exposed Places", placeholder="Enter 1 for Yes, 0 for No")
        

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
    

    
    
    
    
    
    
