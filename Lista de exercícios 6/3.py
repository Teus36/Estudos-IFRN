m = []

for l in range(4):
    linha = [0] * 4
    m.append(linha)

for l in range(4):
    for c in range(4):
        m[l][c] = l * c

for elementos in m:
    print(elementos)