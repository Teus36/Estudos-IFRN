print("=-" * 30)

num = ''
soma = 0
count = 0
par = 0
impar = 0

while num != 0:
    num = float(input("Digite um número: "))
    count += 1
    soma += num
    if num % 2 == 0:
        par += num
    else:
        impar += num
    if num == 0:
        count -= 1

print("=-" * 30)
print(f"A soma de todos os números é {soma}")
print(f"A soma apenas dos números ímpares é {impar}")
print(f"A soma apenas dos números pares é {par}")
print("=-" * 30)
