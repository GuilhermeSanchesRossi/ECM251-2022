class Conta:
    def __init__(self, id = None, historico_compras = [] ):
        self._id = id
        self._historico_compras = historico_compras

    def get_historico_compras(self):
        return self._historico_compras