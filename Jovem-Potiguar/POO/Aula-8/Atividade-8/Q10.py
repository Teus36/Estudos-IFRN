
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

ponto1 = Ponto(1, 2)
ponto2 = Ponto(3, 4)
resultado = ponto1 + ponto2
print(resultado)