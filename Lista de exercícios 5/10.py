l1 = []
l2 = []

for i in range(0, 5):
    l1.append((input(f"Digite o {i+1}º valor da lista 1: ")))
    l2.append((input(f"Digite o {i+1}º valor da lista 2: ")))

soma = l1 + l2
l3 = []

for num in soma:
    if num not in l3:
        l3.append(num)

print(f"Retirando os números repetidos, a lista 3 ficará da seguinte forma: {l3}")