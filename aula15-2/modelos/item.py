class Item():
    def __init__(self, preco, nome, descricao=None): #construtor de classe em py: __init__
        self._nome = nome                   #é possível atribuir valores padrão aos atributos na declaração do construtor
        self._preco = preco                 #o underline _ torna o atributo private
        self._descricao = descricao
    def get_nome(self):
        return self._nome
    def __str__(self):
        return f'Nome: {self._nome} Preço: {self._preco}'   #f indica uma string formatada, como o format em Java
    def get_preco(self):
        return self._preco
    def __eq__(self, __o: object) -> bool:      #método que compara dois objetos, retorna valor booleano
        if isinstance(__o, Item):
            return self._nome == __o.get_nome()
        return False