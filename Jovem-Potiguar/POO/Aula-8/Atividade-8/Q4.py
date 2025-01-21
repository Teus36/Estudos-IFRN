class FormaGeometrica:
    def calcular_area(self):
        return None

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return f"A área do retângulo é: {self.largura * self.altura}"

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return f"A área do círculo é: {3.14159 * (self.raio ** 2)}"


retangulo = Retangulo(5, 10)
circulo = Circulo(7)
print(retangulo.calcular_area())
print(circulo.calcular_area())
