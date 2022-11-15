from src.controllers.usuario_controller import UsuarioController
from src.dao.usuario_dao import UsuarioDAO
from src.models.usuario import Usuario

user_controller = UsuarioController()
user_teste = Usuario("2", "jão", "abc@hotmail.com", "abcd")
user_controller.cadastrar_user(user_teste)
pegar_user = user_controller.procurar_user("2")
print(pegar_user.get_nome())