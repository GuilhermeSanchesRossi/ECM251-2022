from produto import Produto

class Darksouls3(Produto):  #Classe concreta de produto

    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def get_nome(self):
        return super().get_nome()

    def get_preco(self):
        return super().get_preco()
