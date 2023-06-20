m = []
count = 0

for l in range(3):
    linha = [0] * 3
    m.append(linha)

for l in range(3):
    for c in range(3):
        m[l][c] = int(input(f"Digite o valor da posição [{l + 1},{c + 1}]: "))

print("=-" * 10 + " NÚMEROS MAIORES QUE 10 " + "=-" * 10)

for l in range(3):
    for c in range(3):
        if m[l][c] > 10:
            count += 1
            print(f"{m[l][c]}", end=' ')

print(f"Ao total foram {count} números acima de 10")