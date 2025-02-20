
class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        try:
            if "@" in email and ".com" in email:
                self.__email = email
            else:
                raise ValueError("Email inválido.")
        except ValueError as e:
            print(f"Erro: {e}")