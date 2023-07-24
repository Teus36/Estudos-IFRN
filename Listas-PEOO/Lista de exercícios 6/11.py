vogais = [['A', '0', '0', '0', '0'],
          ['0', 'E', '0', '0', '0'],
          ['0', '0', 'I', '0', '0'],
          ['0', '0', '0', 'O', '0'],
          ['0', '0', '0', '0', 'U']]

consoantes = [['B', 'C', 'D', 'F', 'G'],
              ['H', 'J', 'K', 'L', 'M'],
              ['N', 'P', 'Q', 'R', 'S'],
              ['T', 'V', 'W', 'X', 'Y'],
              ['Z', '0', '0', '0', '0']]

nome = "MATEUS"
l_nome = []

for i in range(len(nome)):
    for l in range(5):
        for c in range(5):
            if nome[i] == consoantes[l][c]:
                print(f"{consoantes[l][c]} = Matriz 'consoantes' na posição ({l}, {c})")
                l_nome.append(nome[i])

    for l in range(5):
        for c in range(5):
            if nome[i] == vogais[l][c]:
                print(f"{vogais[l][c]} = Matriz 'vogais' na posição ({l}, {c})")
                l_nome.append(nome[i])

print(l_nome)