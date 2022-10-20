#GUILHERME SANCHES ROSSI/ RA 19.02404-5

from ast import main
import ttkbootstrap as ttk
from login import Login
from darksouls3 import Darksouls3

if __name__ == "__main__":
    x = Darksouls3("sla", 159.90)
    print(x.get_nome)
    tela_login = Login()
    tela_login.rodar()
