saldo = 1000

while saldo > 0:
    print("=-" * 30)
    print(f"SALDO = {saldo}")
    compras = float(input("Digite o valor da sua compra: "))
    if compras > saldo:
        print("ERRO!!! VOCÊ NÃO TEM SALDO O SUFICIENTE PARA ESSA COMPRA")
    else:
        saldo -= compras
        print(f"SALDO = {saldo}")

print("=-" * 30)
print("Saldo zerado")






