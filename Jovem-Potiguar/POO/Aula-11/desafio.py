
class Produto:
    def __init__(self, nome: str, preco: float, cod_barras: str):
        self.__nome = nome
        self.__preco = preco
        self.__cod_barras = None
        self.set_cod_barras(cod_barras)

    def get_nome(self):
        return self.__nome 
    
    def get_preco(self):
        return self.__preco
    
    def get_cod_barras(self):
        return self.__cod_barras 
    
    def set_cod_barras(self, cod_barras):
        try:
            if len(cod_barras) == 8:
                self.__cod_barras = cod_barras
            raise Exception("Código de barra deve conter somente 8 dígitos")
        except Exception as e:
            print(f"Erro: {e}")

class Estoque:
    def __init__(self):
        self.produtos: list[Produto] = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def remover_produto(self):
        try:
            if not self.produtos:
                raise IndexError("O estoque está vazio")
            return self.produtos.pop()
        except IndexError as e:
            print(f"Erro: {e}")
    
    def listar_produtos(self):
        try:
            if not self.produtos:
                raise IndexError("O estoque está vazio")
            else:
                for index, produto in enumerate(self.produtos, start=1):
                    print(f"Nome: {produto.get_nome()} | Preço: {produto.get_preco()} | Código de barras: {produto.get_cod_barras()}")
        except IndexError as e :
            print(f"Erro: {e}")

estoque = Estoque()
produto = Produto("Mouse", 5000, "12345678")
estoque.adicionar_produto(produto)

print("="*20 + " LISTA DE PRODUTOS " + "="*20)
estoque.listar_produtos()

print("="* 59)