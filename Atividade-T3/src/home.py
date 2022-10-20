#GUILHERME SANCHES ROSSI/ RA 19.02404-5

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from produto import Produto
from darksouls3 import Darksouls3

class Home():

    def rodar(self):
        self.__janela_home.mainloop()

    def descricao_produto(self):
        return self.__produto_darksouls3.get_nome+self.__produto_darksouls3.get_preco

    def __init__(self):

        self.__produto_darksouls3 = Darksouls3("Dark Souls 3", 159.90)

        #BASE
        self.__janela_home = ttk.Window(
            title = "Home",
            themename = "vapor",
            position = (700, 300),
            size = (500, 250)
        )

        #LABEL DOS PRODUTOS
        self.__titulo_produtos = ttk.Label(
            self.__janela_home,
            text = "Produtos disponíveis",
            bootstyle = "inverse-warning"
        ).pack(side = LEFT)

        self.__mostrar_produto = ttk.Label(
            self.__janela_home,
            text = self.descricao_produto,
            bootstyle = "inverse-danger"
        ).pack(side = LEFT)

        #LABEL DO CARRINHO DE COMPRAS
        self.__titulo_carrinho = ttk.Label(
            self.__janela_home,
            text = "Carrinho de compras",
            bootstyle = "inverse-warning"
        ).pack(side = RIGHT)