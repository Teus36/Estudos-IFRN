numero_sorteado = int(input("Número sorteado(De 1 a 100): "))
num = ''

while num != numero_sorteado:
    num = int(input("Digite um número: "))
    if num == numero_sorteado:
        print("Parabéns! Você acertou o número sorteado")
    else:
        print("Errou. você não está com sorte")