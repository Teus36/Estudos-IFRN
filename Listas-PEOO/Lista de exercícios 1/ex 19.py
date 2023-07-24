N1 = float(input("Digite quanto você tirou no 1º Bimestre: "))
N2 = float(input("Digite quanto você tirou no 2º Bimestre: "))
N3 = float(input("Digite quanto você tirou no 3º Bimestre: "))
N4 = float(input("Digite quanto você tirou no 4º Bimestre: "))
P2 = 2
P3 = 3
MF = (N1 * P2) + (N2 * P2) + (N3 * P3) + (N4 * P3) / (P2 + P2 + P3 + P3)
print(f"A média final é {MF / 10}")
