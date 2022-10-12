#GUILHERME SANCHES ROSSI/ RA 19.02404-5

from tkinter import BOTTOM, TOP
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from home import Home

class Login():

    def rodar(self):
        self.__janela_login.mainloop()

    def validar_login(self):
        if (self.__email_digitado == "salve@gmail.com") and (self.__senha_digitada == "salve"):
            tela_home = Home()
            tela_home.rodar()
        else:
            print("Dados inválidos!")

    def __init__(self):

        #BASE
        self.__janela_login = ttk.Window(
            title = "Login",
            themename = "vapor",
            position = (700, 300),
            size = (500, 250)
        )

        #BOTÃO DE PROSSEGUIR COM LOGIN
        self.__bot = ttk.Button(
            self.__janela_login,
            text = "Entrar",
            bootstyle = "success",
            command = self.validar_login                 #/quero instanciar página home após login/
        ).pack(side = BOTTOM, padx = 10, pady = 5)

        #LABEL DA ENTRADA DE EMAIL
        self.__titulo_email = ttk.Label(
            self.__janela_login,
            text = "Email",
            bootstyle = "inverse-warning"
        ).pack(side = TOP, padx = 10, pady = 5)

        self.__email_digitado = ""

        #ENTRADA DE EMAIL
        self.__input_email = ttk.Entry(
            self.__janela_login,
            textvariable = self.__email_digitado,
            bootstyle = "warning"
        ).pack(side = TOP)

        #LABEL DA ENTRADA DE SENHA
        self.__titulo_senha = ttk.Label(
            self.__janela_login,
            text = "Senha",
            bootstyle = "inverse-warning"
        ).pack(side = TOP, padx = 10, pady = 5)

        self.__senha_digitada = ""

        #ENTRADA DE SENHA
        self.__input_senha = ttk.Entry(   
            self.__janela_login,
            textvariable = self.__senha_digitada,
            bootstyle = "warning"
        ).pack(side = TOP)