l = []

print("=-" * 30)

for i in range(0, 5):
    l.append(int(input(f"Digite o {i+1}° número: ")))

print("=-" * 30)

for k in range(0, 5):
    print(f"{l[k]} está na posição {k}")


