estoque = []
quantidade_total = 0
valor_total = 0.0

for i in range(5):
    codigo = input("Código do produto: ")
    preco = float(input("Preço do produto: R$"))
    quantidade = int(input("Quantidade do produto: "))

    produto = {
        'codigo': codigo,
        'preco': preco,
        'quantidade': quantidade
    }
    estoque.append(produto)

for produto in estoque:
    quantidade_total += produto['quantidade']
    valor_total += produto['preco'] * produto['quantidade']

print("=-" * 7 + " RELATÓRIO DE ESTOQUE " + "=-" * 8)
print("Código | Preço | Quantidade")
for produto in estoque:
    print(f"{produto['codigo']} | R${produto['preco']:.2f} | {produto['quantidade']}")

print(f"Quantidade total de itens: {quantidade_total}")
print(f"Valor total do estoque: R${valor_total}")
