#GUILHERME SANCHES ROSSI/ RA 19.02404-5

from tkinter import BOTTOM
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Login():

    def rodar(self):
        self.__janela_login.mainloop()

    def __init__(self):
        self.__janela_login = ttk.Window(       #BASE
            title = "Login",
            themename = "yeti",
            position = (700, 300),
            size = (500, 250)
        )
        self.__bot = ttk.Button(        #BOTÃO DE PROSSEGUIR COM LOGIN
            self.__janela_login,
            text = "Entrar",
            bootstyle = "success",
            #command = /quero instanciar página home após login/
        ).pack(side = BOTTOM, padx = 10, pady = 5)
        self.__titulo_email = ttk.Label(        #LABEL DA ENTRADA DE EMAIL
            self.__janela_login,
            text = "Email",
            bootstyle = "inverse-warning"
        ).pack(side = TOP, padx = 10, pady = 5)
        self.__email_digitado = ""
        self.__input_email = ttk.Entry(         #ENTRADA DE EMAIL
            self.__janela_login,
            textvariable = self.__email_digitado,
            bootstyle = "warning"
        ).pack(side = TOP)
        self.__titulo_senha = ttk.Label(        #LABEL DA ENTRADA DE SENHA
            self.__janela_login,
            text = "Senha",
            bootstyle = "inverse-warning"
        ).pack(side = TOP, padx = 10, pady = 5)
        self.__senha_digitada = ""
        self.__input_senha = ttk.Entry(         #ENTRADA DE SENHA   
            self.__janela_login,
            textvariable = self.__senha_digitada,
            bootstyle = "warning"
        ).pack(side = TOP)