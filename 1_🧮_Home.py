import pandas as pd
import streamlit as st
from PIL import Image
##############################################################################
#theme for page 
# we use image as back-ground so we disable primary color and secondary colors for back-ground
#primaryColor="#F63366"
#backgroundColor="#000000"
#secondaryBackgroundColor="#C4CAD0"
#textColor="#FCF7FF"
font="Press Start 2P"    
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be

icon = Image.open("calculator-icon.png")

st.set_page_config(
    page_title="SIMATS Grades Calculator",
    page_icon=icon,
    layout="centered"
)    
st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1523821741446-edb2b68bb7a0?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"); 
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)

c30, c31, c32 = st.columns([0.2, 0.09, 3.2])

with c30:

    st.caption("")

    st.image("calculator-icon.png", width=60)

with c32:

    st.title("SIMATS Grades Calculator")
#table
df = pd.DataFrame(
    [
        {"Grade": "S", "Grade Points": 10},
        {"Grade": "A", "Grade Points": 9},
        {"Grade": "B", "Grade Points": 8},
        {"Grade": "C", "Grade Points": 7},
        {"Grade": "D", "Grade Points": 6},
        {"Grade": "E", "Grade Points": 5},
        {"Grade": "F", "Grade Points": 0},
    ]
)
#grade_input
st.dataframe(df, use_container_width=True)
st.subheader(' ', divider='rainbow')
total_no = st.number_input("Enter Total No of Coures Completed:", 1, 50, "min", 1, placeholder="Insert a number...")
st.write('No of Coures is ', total_no)
user_input_1 = st.number_input("Enter the No of S Grade:", 0, 50, "min", 1, placeholder="Insert a number...")
st.write('No of S Grade is ', user_input_1)
user_input_2 = st.number_input("Enter the No of A Grade:", 0, 50, "min", 1, placeholder="Insert a number...")
st.write('No of A Grade is ', user_input_2)
user_input_3 = st.number_input("Enter the No of B Grade:", 0, 50, "min", 1, placeholder="Insert a number...")
st.write('No of B Grade is ', user_input_3)
user_input_4 = st.number_input("Enter the No of C Grade:", 0, 50, "min", 1, placeholder="Insert a number...")
st.write('No of C Grade is ', user_input_4)
user_input_5 = st.number_input("Enter the No of D Grade:", 0, 50, "min", 1, placeholder="Insert a number...")
st.write('No of D Grade is ', user_input_5)
user_input_6 = st.number_input("Enter the No of E Grade:", 0, 50, "min", 1, placeholder="Insert a number...")
st.write('No of E Grade is ', user_input_6)
user_input_7 = st.number_input("Enter the No of f Grade:", 0, 50, "min", 0, placeholder="Insert a number...")
st.write('No of F Grade is ', user_input_7)
cgpa = 10*user_input_1 + 9*user_input_2 + 8*user_input_3 + 7*user_input_4 + 6*user_input_5 + 5*user_input_6
cpa = cgpa/total_no
#rainbow line
st.subheader(' ', divider='rainbow')
st.write("Your CGPA is",cpa)
#support_text
if(cpa < 7.5):
    st.write("Gambar Gambar Do well in Exam's😉")
elif ((cpa == 8) or (cpa <=8.5)):
    st.write("Well Done My Dear Keep Doing Good🙂")
elif ((cpa >= 8.5) or (cpa <= 9.5) or (cpa == 10)):
    st.write("Excellent Work🤩")    
