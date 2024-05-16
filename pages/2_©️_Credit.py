import streamlit as st

#theme for page 
# we use image as back-ground so we disable primary color and secondary colors for back-ground
#primaryColor="#F63366"
#backgroundColor="#000000"
#secondaryBackgroundColor="#C4CAD0"
textColor="#FCF7FF"
font="Press Start 2P"    

st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1523821741446-edb2b68bb7a0?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"); 
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)

st.set_page_config(page_title="Credits", page_icon="©️")

st.subheader('', divider='rainbow')
st.markdown("""
            **Special Thanks To Streamlit for Free Hosting** \n
            **Server : Streamlit** \n
            **Source: GitHub Open Source Project** \n
            **Any Feedback Please Let us Know in Github Repository** :rainbow[→] [GitHub](https://github.com/Dinakar-22/SIMATS-Grade-Calculato/tree/main)
""")
st.header('~ Thank You ~')
st.subheader('',divider='rainbow')
