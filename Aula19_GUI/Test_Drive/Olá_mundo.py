import ttkbootstrap as ttk
from tkinter import PhotoImage

base = ttk.Window(title = "Minha primeira GUI carai",
    size = (1024, 920),
    position = (512, 100),
    maxsize = (1800, 900),
    minsize = (600, 300),
    alpha = 0.8, #opacidade da tela
    )

base.iconphoto(False, PhotoImage(file = 'calculator.png') )
base.mainloop()