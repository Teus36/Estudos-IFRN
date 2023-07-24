M = []
diagonal_principal = []

for i in range(3):
    linha = []
    for j in range(3):
        letra = input(f"Digite o elemento [{i+1},{j+1}]: ")
        linha.append(letra)
        if i == j:
            diagonal_principal.append(letra)
    M.append(linha)

for linha in M:
    for num in linha:
        print(num, end=" ")
    print()

print("Lista da diagonal principal:", diagonal_principal)