class Usuario:

    def __init__(self, id, nome, email, senha):
        self._id = id
        self._nome = nome
        self._email = email
        self._senha = senha

    def get_email(self):
        return self._email

    def get_senha(self):
        return self._senha
        