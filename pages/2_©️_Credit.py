import streamlit as st

#theme for page 
# we use image as back-ground so we disable primary color and secondary colors for back-ground
#primaryColor="#F63366"
#backgroundColor="#000000"
#secondaryBackgroundColor="#C4CAD0"
textColor="#FCF7FF"
font="Press Start 2P"    

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
