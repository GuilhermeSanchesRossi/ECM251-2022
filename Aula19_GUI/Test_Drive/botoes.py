import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

base = ttk.Window(title = "Minha primeira GUI carai",
    size = (1024, 920),
    position = (512, 100),
    maxsize = (1800, 900),
    minsize = (600, 300),
    alpha = 0.8, #opacidade da tela
    )

base.iconphoto(False, PhotoImage(file = 'calculator.png') )

def acao_Botao():
    print("clicou no botão parabéns")


#criação de botão
ttk.Button(base,
text = "salve",
bootstyle = "default",
command = acao_Botao
).pack(side = LEFT, padx = 10, pady = 5) #subindo o botão à base da interface

#criação de segundo botão
bot2 = ttk.Button(base,
text = "salve 2",
bootstyle = (DANGER, OUTLINE),
command = acao_Botao
)

bot2.pack(side = LEFT, padx = 10, pady = 5)

#ponto de entrada da interface
base.mainloop()