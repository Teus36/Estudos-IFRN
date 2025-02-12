class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Funcionario(Pessoa):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.set_salario(salario)

    def set_salario(self, salario):
        try:
            if salario > 0:
                self.salario = salario
            else:
                raise ValueError("O salário deve ser positivo.")
        except ValueError as e:
            print(f"Erro: {e}")
