l = []
l_inversa = []

for i in range(0, 10):
    l.append(int(input(f"Digite o {i + 1}° número: ")))

count = 10 - 1
while count >= 0:
    l_inversa.append(l[count])
    count -= 1

print(l_inversa)
