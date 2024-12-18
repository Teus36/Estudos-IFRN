nomes = []

print("Digite sair para parar")
while True:
    nome = str(input("Digite um nome: "))
    if nome == 'sair':
        break
    nomes.append(nome)

nomes.sort()
print(f"A lista dos nomes em ordem alfabética é: {nomes}")