from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo.")

class Bicicleta(Veiculo):
    def mover(self):
        print("A bicicleta está se movendo.")

try:
    carro = Carro()
    carro.mover()
except TypeError as e:
    print(f"Erro: {e}")