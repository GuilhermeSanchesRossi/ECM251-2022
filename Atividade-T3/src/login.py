#GUILHERME SANCHES ROSSI/ RA 19.02404-5

from tkinter import BOTTOM, TOP
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from home import Home

class Login():

    def rodar(self):
        self.__janela_login.mainloop()

    def validar_email(self):
        if self.__email_digitado != "lala@gmail.com":
            return False
        else:
            return True

    def validar_senha(self):
        if self.__senha_digitada != "1234":
            return False
        else:
            return True

    def command_bot_entrar(self):
        self.__tela_home = Home()
        self.__tela_home.rodar()

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
            command = self.command_bot_entrar          #quero instanciar página home após login
        ).pack(side = BOTTOM, padx = 10, pady = 5)

        self.__validador_email = self.__janela_login.register(self.validar_email)       #vi na documentação que isso é necessário

        self.__email_digitado = ""

        #LABEL DA ENTRADA DE EMAIL
        self.__titulo_email = ttk.Label(
            self.__janela_login,
            text = "Email",
            bootstyle = "inverse-warning"
        ).pack(side = TOP, padx = 10, pady = 5)

        #ENTRADA DE EMAIL
        self.__input_email = ttk.Entry(
            self.__janela_login,
            textvariable = self.__email_digitado,
            validate = "focus",                                 #comando para que, ao se digitar o dado inválido,
            validatecommand = (self.__validador_email, '%P'),   #o entry widget se torna vermelho nas bordas
            bootstyle = "warning"
        ).pack(side = TOP)

        self.__senha_digitada = ""

        self.__validador_senha = self.__janela_login.register(self.validar_senha)

        #LABEL DA ENTRADA DE SENHA
        self.__titulo_senha = ttk.Label(
            self.__janela_login,
            text = "Senha",
            bootstyle = "inverse-warning"
        ).pack(side = TOP, padx = 10, pady = 5)

        #ENTRADA DE SENHA
        self.__input_senha = ttk.Entry(   
            self.__janela_login,
            textvariable = self.__senha_digitada,
            validate = "focus",
            validatecommand = (self.__validador_senha, '%P'),
            bootstyle = "warning"
        ).pack(side = TOP)