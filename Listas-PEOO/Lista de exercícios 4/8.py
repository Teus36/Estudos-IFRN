letras_n = []
letras_s = []

nome = str(input("Digite o seu nome: "))
sobrenome = str(input("Digite o seu sobrenome: "))

for n in range(0, len(nome)):
    letras_n.append(nome[n])

for s in range(0, len(sobrenome)):
    letras_s.append(sobrenome[s])

conc = letras_n + letras_s

print(f"O nome possui {len(letras_n)} letras", end='')
print(f" e o sobrenome possui {len(letras_s)} letras")
print(f"Seu nome completo é {conc}")

