
class User:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha 

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_senha(self, senha):
        self.__senha = senha 

    def get_nome(self):
        return self.__nome 

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha 
    
    def atualizar_informacoes(self, nome, email, senha):
        if nome and email and senha:
            self.set_nome(nome)
            self.set_email(email)
            self.set_senha(senha)
        print("Informações atualizadas com sucesso!!!")

    def exibir_informações(self, nome, email, senha):
        if nome and email and senha:
            self.get_nome(nome)
            self.get_email(email)
            self.get_senha(senha)

    def apresentacao_informacoes(self, nome, email, senha):
        pass
    

nome = str(input("Digite um nome: "))
email = str(input("Digite seu endereço de email: "))
senha = str(input("Digite sua senha: "))


User(nome, email, senha)
User.exibir_informações()


