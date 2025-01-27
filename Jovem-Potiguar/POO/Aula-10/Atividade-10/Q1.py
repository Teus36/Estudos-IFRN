
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo 

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo
    
    def set_titular(self, titular):
        self.__titular = titular

    def set_saldo(self, valor):
        try:
            if valor < 0:
                raise ValueError("O saldo deve ser positivo")
                self.__saldo = valor

        except ValueError as e:
            print(f"Erro: {e}")

user1 = ContaBancaria("Mateus", "3000")
print(f"Titular: {user1.get_titular()}\nSaldo: R${user1.get_saldo()}")