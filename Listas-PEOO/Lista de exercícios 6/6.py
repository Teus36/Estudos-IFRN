m = []
soma = 0

for l in range(3):
    linha = [0] * 3
    m.append(linha)

for l in range(3):
    for c in range(3):
        m[l][c] = int(input(f"Digite o valor da posição [{l + 1},{c + 1}]: "))

for i in range(3):
    soma += m[i][2-i]

print(f"A soma dos elementos da diagonal secundária é : {soma}")