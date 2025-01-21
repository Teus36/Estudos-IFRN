
class Produto:
    def __init__(self, nome, preco=None):
        self.nome = nome
        if preco is None:
            self.preco = 0
        else:
            self.preco = preco


produto1 = Produto("Notebook")
produto2 = Produto("Celular", 2500)
print(produto1.nome, produto1.preco)
print(produto2.nome, produto2.preco)