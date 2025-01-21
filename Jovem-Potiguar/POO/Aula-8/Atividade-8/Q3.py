
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    
    def cumprimentar(self):
        print(f"Olá me chamo {self.nome} e tenho {self.idade} anos.")

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def cumprimentar(self):
        super().cumprimentar()
        print(f"Minha matrícula é {self.matricula}")
    

estudante = Estudante("Ana", 21, "20230001")
estudante.cumprimentar()