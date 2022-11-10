from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

class UsuarioController:

    def __init__(self) -> None:
        pass

    def comparar_Email(self, email) -> bool:
        instancia1 = UsuarioDAO.get_instance()
        return instancia1.comparar_email(email)

    def comparar_Senha(self, senha) -> bool:
        instancia2 = UsuarioDAO.get_instance()
        return instancia2.comparar_senha(senha)