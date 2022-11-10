import streamlit as st

class PaginaLogin:

    def __init__(self):
        st.title("Faça seu login")
        self._email = st.text_input(label = "email")
        self._senha = st.text_input(label = "senha")