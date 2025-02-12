from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class Operador(Funcionario):
    def __init__(self, nome, horas, valor_hora):
        self.nome = nome
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas * self.valor_hora

gerente = Gerente("Maria", 5000)
operador = Operador("José", 20, 50)
print(gerente.calcular_salario())
print(operador.calcular_salario())