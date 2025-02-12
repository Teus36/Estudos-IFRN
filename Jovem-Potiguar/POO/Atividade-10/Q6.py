from abc import ABC, abstractmethod

class Conta(ABC):
    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor + 2.50 <= self.saldo:
            self.saldo -= (valor + 2.50)
        else:
            print("Saldo insuficiente.")

class ContaPoupanca(Conta):
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.saques_gratuitos = 3

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saques_gratuitos > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.saques_gratuitos -= 1
            else:
                print("Saldo insuficiente.")
        else:
            if valor + 5.00 <= self.saldo:
                self.saldo -= (valor + 5.00)
            else:
                print("Saldo insuficiente.")
