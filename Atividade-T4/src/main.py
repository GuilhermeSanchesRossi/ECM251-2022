from src.models.produto import Produto
from src.dao.produto_dao import ProdutoDAO
from src.controllers.produto_controller import ProdutoController

teste_controller = ProdutoController()
produto_teste = Produto(id="2", preco=159.90, nome="seila2", descricao="mt foda 2")
teste_controller.cadastrar_prod(produto_teste)
pegar_produto = teste_controller.procurar_prod("2")
print(pegar_produto.get_nome())