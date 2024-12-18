

while True:
    print(""
          "[ 1 ] SOMAR \n"
          "[ 2 ] SUBTRAIR \n"
          "[ 3 ] MULTIPLICAR \n"
          "[ 4 ] DIVIDIR \n"
          "[ 5 ] SAIR")
    opcao = int(input("Escolha uma das opções acima: "))

    if opcao == 5:
        break

    if opcao not in [1, 2, 3, 4]:
        print("Opção inválida. Tente novamente.")
        continue

    n1 = float(input("Digite um primeiro número: "))
    n2 = float(input("Digite um segundo número: "))

    if opcao == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
    if opcao == 2:
        subtracao = n1 - n2
        print(f"{n1} - {n2} = {subtracao}")
    if opcao == 3:
        multiplicacao = n1 + n2
        print(f"{n1} * {n2} = {multiplicacao}")
    if opcao == 4:
        divisao = n1 / n2
        print(f"{n1} / {n2} = {divisao}")