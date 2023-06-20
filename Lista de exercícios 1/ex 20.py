cateto1 = int(input("Digite o valor do primeiro cateto: "))
cateto2 = int(input("Digite o valor do segundo cateto: "))
h = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
print(f"A hipotenusa desse triângulo é {h:5.2f}")