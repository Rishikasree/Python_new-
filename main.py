import streamlit as st
import pandas as pd  
from streamlit_option_menu import option_menu

col1,col2 = st.columns(2)
with st.sidebar:
    selected = option_menu(
        menu_title = "Research Project",
        options= ["Demographic profile","About talent acquisition","Scale question"]
    )

if selected == "Demographic profile":
        
        with col1:
         st.header("Enter your details")
         name = st.text_input("Name:")
         age = st.number_input("Age:", min_value=0,max_value=50,step=1)
         gender = st.selectbox("Gender:",["Male", "Female"])
         ms = st.selectbox("Marital status:",["Married","Unmarried"])
         qualification = st.selectbox("Qualification:",["UG","PG"])
        with col2:
         salary = st.selectbox("Salary:",["10-15k","15-20k","Above 20k"])
         locality = st.selectbox("Locality:",["Rural","Urban","Semi urban"])
         we = st.selectbox("Work experience:",["1-2 years","2-5 years","More than 5 years"])
         os = st.selectbox("Occupation status:",["Full time","Part time"])
         d = st.selectbox("Designation:",["Developer","Data analyst","Tech lead","Admin","Tech trainees","Non tech staff","Business development executive"])
        reg = st.button("Register")
        if reg:
            st.write("Profile saved")
        data = {
            "Name" : [name],
            "Age"  :  [age],
            "Gender" : [gender],
            "MS": [ms],
            "Qualification": [qualification],
            "Salary": [salary],
            "Locality": [locality],
            "Work experience": [we],
            "Occupation status": [os],
            "Designation": [d],
        }
        df = pd.DataFrame(data)
        st.write(df)

elif selected == "About talent acquisition":
           st.write("Give the answers")
           program = st.selectbox("Program attended:",["1-2","5-10","More than 10"])
           mode = st.selectbox("Mode of program:",["In person","Online","Both"])
           outcome = st.selectbox("Outcome of the program:",["Minimal","Moderate","Significant"])
           person = st.selectbox("Responsible person for program:",["Internal employees","T&D team","External consultants"])
           purpose = st.selectbox("Primary purpose of development program:",["To enhance skills & knowledge","To improve performance & productivity","To support talent acquisition & retention"])
           ok = st.button("Click me")
           if ok:
             st.write(f"Program attended:{program}")
             st.write(f"Mode of program:{mode}")
             st.write(f"Outcome of program:{outcome}")
             st.write(f"Responsible person for program:{person}")
             st.write(f"Primary purpose of program:{purpose}")

elif selected == "Scale question":
          st.write("DEVELOPMENT PROGRAM INFORMATION")
          q1 = st.checkbox("Rate the quality of development program")
          q2 = st.checkbox("Whether it is accessible for current job role")
          q3 = st.checkbox("Support career advancement & growth in organization")
          q4 = st.checkbox("Effective in enhancing skills & knowledge")
          q5 = st.checkbox("Rate the expertise of trainer")
          st.write("EFFECTIVENESS OF PROGRAM IN TALENT ACQUISITION")
          q6 = st.checkbox("Development program align with business goals")
          q7 = st.checkbox("Evaluation process of development program organization")
          q8 = st.checkbox("Program contribute to successful talent acquisition")
          q9 = st.checkbox("Program provide a positive return on investment")
          q10 = st.checkbox("Development program contribute to talent retention")
          q11 = st.checkbox("You feel engaged & motivated throughout the program ")
          q12 = st.checkbox("Delivered about new technological advancement in a particular designation")
          st.write("IMPACT OF DEVELOPMENT PROGRAM ON TALENT ACQUISITION")
          q13 = st.checkbox("Enhance cultural competence on other department employees")
          q14 = st.checkbox("Development program contribute to create inclusive workplace")
          q15 = st.checkbox("Encourages employee engagement with diversity & inclusion")
          q16 = st.checkbox("Program helps to recognize & overcome unconsious biases")
          q17 = st.checkbox("Was it effective in developing leadership skills")
          q18 = st.checkbox("Improved perception of diversity & inclusion in workplace")
          q19 = st.checkbox("Helps to recognize & address micro agressions in workplace")
          q20 = st.checkbox("Confident in applying the concept learned during program")
          s1 = st.button("Submit")
          if s1:
             st.write(f"Rate the quality of development program {'A' if q1 else 'D'}")
             st.write(f"Whether it is accessible for current job role {'A' if q2 else 'D'}")
             st.write(f"Support career advancement & growth in organization {'A' if q3 else 'D'}")
             st.write(f"Effective in enhancing skills & knowledge {'A' if q4 else 'D'}")
             st.write(f"Rate the expertise of trainer {'A' if q5 else 'D'}")
             st.write(f"Development program align with business goals {'A' if q6 else 'D'}")
             st.write(f"Evaluation process of development program organization {'A' if q7 else 'D'}")
             st.write(f"Program contribute to successful talent acquisition {'A' if q8 else 'D'} ")
             st.write(f"Program provide a positive return on investment{'A' if q9 else 'D'} ")
             st.write(f"Development program contribute to talent retention {'A' if q10 else 'D'} ")
             st.write(f"You feel engaged & motivated throughout the program{'A' if q11 else 'D'}  ")
             st.write(f"Delivered about new technological advancement in a particular designation {'A' if q12 else 'D'}")
             st.write(f"Enhance cultural competence on other department employees {'A' if q13 else 'D'}")
             st.write(f"Development program contribute to create inclusive workplace {'A' if q14 else 'D'}")
             st.write(f"Encourages employee engagement with diversity & inclusion {'A' if q15 else 'D'}")
             st.write(f"Program helps to recognize & overcome unconsious biases {'A' if q16 else 'D'}")
             st.write(f"Effective in developing leadership skills {'A' if q17 else 'D'}")
             st.write(f"Improved perception of diversity & inclusion in workplace {'A' if q18 else 'D'}")
             st.write(f"Helps to recognize & address micro agressions in workplace {'A' if q19 else 'D'}")
             st.write(f"Confident in applying the concept learned during program {'A' if q20 else 'D'}")
             

       


        