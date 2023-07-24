A = []
B = []
C = []

print("Digite os elementos da matriz A")
for l in range(3):
    linha_A = []
    for c in range(3):
        num_A = int(input(f"Digite o valor do elemento [{l+1},{c+1}]: "))
        linha_A.append(num_A)
    A.append(linha_A)

print("Digite os elementos da matriz B:")
for l in range(3):
    linha_B = []
    for c in range(3):
        num_B = int(input(f"Digite o valor do elemento [{l+1},{c+1}]: "))
        linha_B.append(num_B)
    B.append(linha_B)

for i in range(3):
    linha_C = []
    for j in range(3):
        num_A = A[i][j]
        num_B = B[i][j]
        if num_A >= num_B:
            maior_elemento = num_A
        else:
            maior_elemento = num_B
        linha_C.append(maior_elemento)
    C.append(linha_C)

print("Terceira matriz:")
for linha in C:
    print(linha)