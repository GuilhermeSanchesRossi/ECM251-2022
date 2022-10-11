from tkinter import BOTTOM
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Login():

    def rodar(self):
        self.janela_login.mainloop()

    def _criar_input(self, string):
        return ttk.Entry(
            self.janela_login,
            textvariable = string
        )

    def __init__(self):
        self.janela_login = ttk.Window(
            title = "Login",
            themename = "yeti",
            position = (700, 300),
            size = (500, 500)
        )
        self.bot = ttk.Button(
            self.janela_login,
            text = "Entrar",
            bootstyle = "success",
            #command = /quero instanciar página home após login/
        ).pack(side = BOTTOM, padx = 10, pady = 5)
        self.valor_digitado = ""
        self.input = self._criar_input(string = self.valor_digitado)
    