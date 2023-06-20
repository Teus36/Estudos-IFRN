linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

A = []
B = []

for l in range(linhas):
    linha = []
    for c in range(colunas):
        num = int(input(f"Digite o valor do elemento [{l+1}:{c+1}]: "))
        linha.append(num)
    A.append(linha)

for i in range(colunas):
    linha_t = []
    for j in range(linhas):
        linha_t.append(A[j][i])
    B.append(linha_t)

print("Matriz A:")
for linha in A:
    print(linha)

print("Matriz B (transposta de A):")
for linha in B:
    print(linha)

