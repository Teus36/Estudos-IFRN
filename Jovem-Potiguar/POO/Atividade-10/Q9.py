
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.set_nota(nota)

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        try:
            if 0 <= nota <= 10:
                self.__nota = nota
            else:
                raise ValueError("A nota deve estar entre 0 e 10.")
        except ValueError as e:
            print(f"Erro: {e}")
