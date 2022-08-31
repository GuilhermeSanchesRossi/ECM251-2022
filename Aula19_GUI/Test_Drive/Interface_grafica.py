import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class MinhaUI():
    def acao_botao(self):
        print("Clicou no botão parabéns")

    def _construir_base(self):
        janela = ttk.Window(
            title = "Minha primeira GUI carai",
            size= (1024,920),
            position = (512,100),
            minsize = (600,300),
            maxsize = (1800,900),
            alpha = 0.9
        )
        janela.iconphoto(False, PhotoImage(file='calculator.png'))
        return janela

    def __init__(self) -> None:
        self.base = self._construir_base()
        #Criando um botão
        ttk.Button(
            self.base,
            text="salve!",
            bootstyle="default",
            command=self.acao_botao
        ).pack(side=LEFT, padx= 10, pady=5)

        #Criando um segundo botão
        self.bot2 = ttk.Button(
            self.base,
            text="salve2",
            bootstyle=(DANGER,OUTLINE),
            command=self.acao_botao
        )
        self.bot2.pack(side=LEFT, padx= 10, pady = 5)
    def run(self):
        self.base.mainloop()

    def ativar_bot(self):
        print("Ligando botao!")
        self.bot2.configure(state="enabled")
    def desativar_bot(self):
        print("Desligando botao!")
        self.bot2.configure(state="disabled")

if __name__ == "__main__":
    app = MinhaUI()
    app.run()