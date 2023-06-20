print("=-" * 30)
l = []
for i in range(0, 5):
    l.append(int(input(f"Digite o {i + 1}° número: ")))

print("=-" * 30)

maior = l[0]
menor = l[0]

for num in l:
    if num > maior:
        maior = num

for num in l:
    if num < menor:
        menor = num

print(f"Os números digitados foram {l}")
print(f"O maior número foi {maior}")
print(f"O menor número foi {menor}")
print("=-" * 30)