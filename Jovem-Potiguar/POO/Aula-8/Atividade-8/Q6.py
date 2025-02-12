
class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

class Pessoa:
    def __init__(self, nome, idade, endereco, carro):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        print(f"Endereço: {self.endereco.rua}, {self.endereco.cidade}, {self.endereco.estado}")


endereco = Endereco("Rua A", "São Paulo", "SP")
pessoa = Pessoa("João", 30, endereco)
pessoa.exibir_dados()