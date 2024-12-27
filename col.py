import streamlit as st


col1,col2 = st.columns(2)

with col1:
    st.text_input('Name')
    st.text_input('Email')

with col2:
    st.text_input('Number')
    st.text_input('Password')

st.button('Submit')