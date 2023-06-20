print("=-" * 30)

num = ''
soma = 0
count = 0

while num != 0:
    num = float(input("Digite um número (Digite 0 para sair): "))
    count += 1
    soma += num
    if num == 0:
        count -= 1

print("=-" * 30)
print(f"A soma entre todos os números digitados é {soma}")
print(f"A média desses números é {soma/count}")