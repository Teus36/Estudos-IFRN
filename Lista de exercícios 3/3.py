num = int(input("Digite um número: "))
f = num
fatorial = 1

print("=-" * 30)

print(f"O fatorial desse número é {num}! = ", end='')
while f > 0:
    print(f"{f}", end='')
    if f > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= f
    f -= 1

print(f"{fatorial}", end='')

