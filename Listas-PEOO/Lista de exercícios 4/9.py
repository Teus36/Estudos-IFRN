num = int(input("Digite um número (maior que 1000): "))
conv = str(num)

while num < 1000:
    print("O número digitado não é maior que 1000. Tente novamente !!!")
    num = int(input("Digite um número (maior que 1000): "))
    conv = str(num)

num_inv = conv[::-1]
num = int(num_inv)
print(f"Resultado: {num}")



