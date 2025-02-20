
class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        try:
            if produto in self.produtos:
                self.produtos.remove(produto)
            else:
                raise ValueError("Produto não encontrado no estoque.")
        except ValueError as e:
            print(f"Erro: {e}")
