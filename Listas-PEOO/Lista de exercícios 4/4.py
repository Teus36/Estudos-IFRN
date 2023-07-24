l = []

for i in range(0, 5):
    l.append(int(input(f"Digite o {i + 1}º número da lista: ")))

for k in range(0, 5):
    for j in range(k + 1, 5):
        if l[k] > l[j]:
            troca_de_posicoes = l[k]
            l[k] = l[j]
            l[j] = troca_de_posicoes

print(l)
