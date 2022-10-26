from src.controllers.pedido_controller import PedidoController

controller = PedidoController()
#Exibe os itens de um pedido
resultado = controller.pegar_pedido("001")
for elemento in resultado:
    print(elemento)

item_novo = resultado[0]
item_novo.quantidade = 10
print(controller.atualizar_pedido(item_novo))
print("***********************************")
resultado = controller.pegar_pedido("001")
for elemento in resultado:
    print(elemento)