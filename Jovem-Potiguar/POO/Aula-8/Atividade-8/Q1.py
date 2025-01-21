
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")

carro1 = Carro("Toyota", "Corolla", 2020)
carro1.exibir_dados()