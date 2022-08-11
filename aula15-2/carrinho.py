class Carrinho():
    def __init__(self):
        self._items = []
    def get_valor_total(self):
        total = 0
        for item in self._items:
            total += item.get_preco()
        return total
    def get_tamanho(self):
        return len(self._items)
    def adicionar(self, item):
        self._items.append(item)        #como items é um atributo lista, os métodos append()e len() não precisam ser definidos
    def remover(self, item):
        self._items.remove(item)
    