frutas = ['maçã', 'banana', 'laranja', 'uva']

print(f"Lista de frutas: {frutas}")

posicao = 0
tamanho = len(frutas)

while posicao < tamanho:
    print(f"Removendo {frutas[0]}")
    frutas.pop(0)
    posicao += 1

