notas = []

for i in range(0, 4):
    notas.append(int(input(f"Digite a nota do  {i + 1}º bimestre: ")))

soma = notas[0] + notas[1] + notas[2] + notas[3]
media = soma/len(notas)

maior = notas[0]
menor = notas[0]

for num in notas:
    if num > maior:
        maior = num

for num in notas:
    if num < menor:
        menor = num

print(f"A média foi de: {media}")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")