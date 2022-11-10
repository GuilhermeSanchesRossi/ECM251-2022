import streamlit as st

class PaginaLogin:

    def __init__(self):
        st.title("Faça seu login")
        st.text_input(label = "email")
        st.text_input(label = "senha")