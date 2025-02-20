class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        try:
            if preco > 0:
                self.__preco = preco
            else:
                raise ValueError("O preço deve ser maior que zero.")
        except ValueError as e:
            print(f"Erro: {e}")