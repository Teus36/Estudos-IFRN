n1 = float(input("Digite um primeiro número: "))
n2 = float(input("Digite um segundo número: "))
operacao = str(input("Digite a operação que você deseja realizar (somar, subtrair, multiplicar e dividir): "))

if operacao == "somar":
    soma = n1 + n2
    print(f"{n1} + {n2} = {soma}")
elif operacao == "subtrair":
    subtracao = n1 - n2
    print(f"{n1} - {n2} = {subtracao}")
elif operacao == "multiplicar":
    multiplicacao = n1 + n2
    print(f"{n1} * {n2} = {multiplicacao}")
elif operacao == "dividir":
    divisao = n1 / n2
    print(f"{n1} / {n2} = {divisao}")
else:
    print("ERRO!!! DIGITE UMA OPERAÇÃO VÁLIDA")