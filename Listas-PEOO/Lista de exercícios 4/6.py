l = []

for i in range(0, 5):
    l.append(int(input(f"Digite o {i + 1}° número da lista: ")))

num = int(input("Agora digite um número qualquer: "))

if num in l:
    print(f"O número {num} está na lista")
else:
    print(f"O número {num} não está na lista")