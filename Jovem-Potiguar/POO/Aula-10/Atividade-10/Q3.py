
class EmailInvalido(Exception):
    def __init__(self, mensagem):
        super().__init__(self.mensagem)
        self.mensagem = mensagem

class Usuario:
    def __init__(self, nome, email: str):
        self.__nome = nome
        self.__email = None
        self.set_email(email)

    def get_nome(self):
        return self.__nome 
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        try:
            if ("@" not in email) or (".com" not in email):
                raise EmailInvalido("Email inválido")
            self.__email = email
        except EmailInvalido as e:
            print(f"Erro: {e}")

        except TypeError as e:
            print(f"Erro: {e}")






