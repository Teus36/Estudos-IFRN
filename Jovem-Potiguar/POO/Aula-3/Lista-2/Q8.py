nota = float(input("Digite a nota que você tirou: "))

if nota >= 9:
    print("Excelente")
elif 7 <= nota < 9:
    print("Bom")
elif 5 <= nota < 7:
    print("Regular")
else:
    print("Reprovado")


