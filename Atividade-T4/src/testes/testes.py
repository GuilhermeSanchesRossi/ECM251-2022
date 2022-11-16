from src.controllers.usuario_controller import UsuarioController
from src.dao.usuario_dao import UsuarioDAO
from src.models.usuario import Usuario


user_controller = UsuarioController()
user_teste = Usuario("1", "jão", "abc@hotmail.com", "abcd")
user_controller.cadastrar_user(user_teste)
pegar_user = user_controller.procurar_user("jão")
print(pegar_user.get_nome())
print(pegar_user.get_id())

user_teste2 = Usuario("2", "zé", "zé@yahoo.com", "aaa")
user_controller.cadastrar_user(user_teste2)
pegar_user2 = user_controller.procurar_user("zé")
print(pegar_user2.get_nome())
print(pegar_user2.get_id())


user_teste3 = Usuario("3", "ba", "ba@hotmail.com", "bbb")
user_controller.cadastrar_user(user_teste3)
pegar_user = user_controller.procurar_user("ba")
print(pegar_user.get_nome())
print(pegar_user.get_id())
