
class Empregado:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.set_salario(salario)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        try:
            if salario > 0:
                self.__salario = salario
            else:
                raise ValueError("O salário deve ser maior que zero.")
        except ValueError as e:
            print(f"Erro: {e}")

# Questão 8: Gerenciamento de estoque
class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        try:
            if produto in self.produtos:
                self.produtos.remove(produto)
            else:
                raise ValueError("Produto não encontrado no estoque.")
        except ValueError as e:
            print(f"Erro: {e}")