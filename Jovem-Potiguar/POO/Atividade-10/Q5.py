
class Login:
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = senha

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        try:
            if len(senha) >= 6:
                self.__senha = senha
            else:
                raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        except ValueError as e:
            print(f"Erro: {e}")
