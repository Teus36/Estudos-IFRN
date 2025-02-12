
while True:
    try:
        num1 = int(input("Digite um primeiro número: "))
        num2 = int(input("Digite um segundo número: "))
        div = num1 / num2 
        print(f"A dvisão entre os dois números é: {div}")
        break

    except ValueError:
        print(f"Erro: Você precisa digitar um número")

    except ZeroDivisionError:
        print("ERRO: Não é possível dividir um número por 0")
