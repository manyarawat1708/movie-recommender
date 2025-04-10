import streamlit as st

st.title('Movie recommender system')
option = st.selectbox(
    'How you like to be contected?',
    ('Email','Phone number','contact info')
)