num = ''
count = 0
p1 = p2 = p3 = p4 = 0

while num != 0:

    num = float(input("Digite um número (Digite 0 para sair): "))
    count += 1
    if num == 0:
        count -= 1

    if num > 0:
        if 25 >= count >= 1:
            p1 += 1
        elif 50 >= count >= 25:
            p2 += 1
        elif 75 >= count >= 51:
            p3 += 1
        elif 100 >= count >= 76:
            p4 += 1

print(f'Entre o intervalo [1-25] há: {p1} positivos')
print(f'Entre o intervalo [26-50] há: {p2} positivos')
print(f'Entre o intervalo [51-75] há: {p3} positivos')
print(f'Entre o intervalo [76-100] há: {p4} positivos')







