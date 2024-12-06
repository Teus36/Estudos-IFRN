temperaturas = [30, 25, 28, 35, 22, 27]

posicao = 0
soma = 0

while posicao < len(temperaturas):
    soma = soma + temperaturas[posicao]
    posicao += 1

media = soma/ len(temperaturas)
print(f"A média das temperaturas é: {media}")