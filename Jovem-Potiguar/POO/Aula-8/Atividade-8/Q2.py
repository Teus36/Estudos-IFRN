
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    # Getters 

    def get_saldo(self):
        return self.__saldo

    # Setters 

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor



conta = ContaBancaria("João", 1000)
conta.depositar(600)
conta.sacar(200)
print(conta.get_saldo())


