#Criação de interface apenas para teste

from cgitb import text
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class UIlojinha():

    def _construir_base(self):
        janela = ttk.Window(
            title ="Loja do carai",
            size = (1024,400),
            position = (0,0),
            minsize = (600,300),
            maxsize = (1800,900),
            alpha = 1.0
        )
        return janela

    def __init__(self) -> None:
        self.janela = self._construir_base()

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = UIlojinha()
    app.run()