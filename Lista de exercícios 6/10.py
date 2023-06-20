palavra = input("Digite uma palavra: ")
matriz = [['X'] * 4 for x in range(4)]
i = 0

for l in range(4):
    for c in range(4):
        if i < len(palavra):
            matriz[l][c] = palavra[i]
            i += 1

for linha in matriz:
    for num in linha:
        print(num, end=' ')
    print()