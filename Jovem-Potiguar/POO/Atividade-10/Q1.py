
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        try:
            if valor > 0:
                self.__saldo += valor
            else:
                raise ValueError("O valor do saldo deve ser positivo.")
        except ValueError as e:
            print(f"Erro: {e}")


conta = ContaBancaria("João")
conta.set_saldo(-50)
