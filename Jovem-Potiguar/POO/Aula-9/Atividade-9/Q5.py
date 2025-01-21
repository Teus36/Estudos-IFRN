
while True:
    try:
        num1 = int(input("Digite um primeiro número: "))
        num2 = int(input("Digite um segundo número: "))
        soma = num1 + num2
        print(f"A soma dos dois números é: {soma}")
        break

    except ValueError:
        print(f"Erro: Você precisa digitar um número")