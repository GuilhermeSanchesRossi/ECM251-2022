from controllers.usuario_controller import UsuarioController
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

teste_controller = UsuarioController()
user_teste = Usuario(1, 'guizao', 'seila@gmail.com', 'coxinha123')
bool1 = teste_controller.comparar_Email(user_teste.get_email())
bool2 = teste_controller.comparar_Senha(user_teste.get_senha())
print(bool1)
print(bool2)