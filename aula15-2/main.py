from modelos.item import Item       # Convenção em py: nome de arquivo começa em minúsculo; classe começa com maiúsculo
from modelos.carrinho import Carrinho

#Diferentes possibilidades de instanciação
#Se vc especificar a variável, não é necessário fazer na ordem a instanciação delas
item1 = Item(preco=80, nome="Dark Souls", descricao="mt foda")
item2 = Item(nome="Dark Souls 2 Scholar of the Fist Sin", descricao = "foda", preco=70)
item3 = Item(250, "Elden Ring", "Masterpiece")
item4 = Item(100, "dark Souls 3")   #descricao já foi pré atribuido com None

print(item1)    #funciona se der override no método __str__(), que é o toString()

carrinho1 = Carrinho()
print("Valor total atual no carrinho:", carrinho1.get_valor_total())
carrinho1.adicionar(item1)
carrinho1.adicionar(item3)
tamanho = carrinho1.get_tamanho()
print("Quantos itens há:", tamanho)
print("Valor total atual no carrinho:", carrinho1.get_valor_total())

print(item1 == item2)       #comparação lógica que só é possível com o método __eq__()
print(item2 == "Dark Souls 2 Scholar of the Fist Sin")  #deve retornar False, pois a string não é uma instância de objeto item, apesar de ser o mesmo nome