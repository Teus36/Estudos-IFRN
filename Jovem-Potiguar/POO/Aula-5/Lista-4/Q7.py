numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobrados = []
contador = 0

while contador < len(numeros):
    dobrar = numeros[contador] * 2
    dobrados.append(dobrar)
    contador += 1

print(f"O dobro de cada valor da primeira lista é: {dobrados}")

