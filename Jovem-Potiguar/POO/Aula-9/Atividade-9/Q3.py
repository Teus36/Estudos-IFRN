
while True:
    try:
        num1 = int(input("Digite um primeiro número: "))
        num2 = int(input("Digite um segundo número: "))
        div = num1 / num2 
        print(f"A divisão do primeiro número pelo segundo é: {div}")
        break

    except ZeroDivisionError:
        print("ERRO!!! Não é possível dividir um número por 0")

    