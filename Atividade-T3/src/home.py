#GUILHERME SANCHES ROSSI/ RA 19.02404-5

import ttkbootstrap as ttk

class Home():

    def rodar(self):
        self.__janela_home.mainloop()

    def __init__(self):

        self.__janela_home = ttk.Window(
            title = "Home",
            themename = "vapor",
            position = (700, 300),
            size = (500, 250)
        )