from abc import ABC, abstractmethod

class Produto(ABC): #Classe abstrata de produto

    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco