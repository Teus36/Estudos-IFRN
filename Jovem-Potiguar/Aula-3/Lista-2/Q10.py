n1 = int(input("Digite um número: "))
advinhar = int(input("Tente advinhar o número escolhido: "))

if advinhar < n1:
    print("Muito baixo")
elif advinhar > n1:
    print("Muito alto")
else:
    print("Você acertou")