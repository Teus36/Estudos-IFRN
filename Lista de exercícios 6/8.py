nome = input("Digite o seu primeiro nome: ")
t_nome = len(nome)

M = []
i = 0

for l in range(4):
    linha = []
    for c in range(4):
        letra = nome[i % len(nome)]
        linha.append(letra)
        i += 1
    M.append(linha)

for linha in M:
    print(linha)