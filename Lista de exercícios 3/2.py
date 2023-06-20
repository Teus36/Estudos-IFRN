print("=-" * 30)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while num2 <= num1:
    print("ERRO! DIGITE UM NÚMERO MAIOR QUE O PRIMEIRO")
    num2 = int(input("Digite o segundo número: "))

print("=-" * 30)
if (num1 % 2 == 0) and (num2 % 2 == 0):
    soma = num1 + num2
    print(f"A soma dos números pares é {soma}")