numeros_inseridos = []

while True:
    n = int(input("Insira um número: "))
    if n == 0:
        break
    numeros_inseridos.append(n)

print(numeros_inseridos)

posicao = 0
soma = 0

while posicao < len(numeros_inseridos):
    soma = soma + numeros_inseridos[posicao]
    posicao += 1

print(f"Lista dos numeros_inseridos: {numeros_inseridos}")
print(f"A soma dos números inseridos é: {soma}")