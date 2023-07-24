print("=-" * 30)
deposito_inicial = float(input("Depósito inicial: R$"))
juros = float(input("Qual é a taxa de juros mensal? "))
mes = 1
saldo = deposito_inicial

print("=-" * 30)

while mes <= 12:
    saldo = saldo + (saldo * (juros/100))
    print(f"O saldo do mês {mes} foi de R${saldo:5.2f}")
    mes += 1

print("=-" * 30)
print(f"O total que foi ganho com os juros foi de {saldo - deposito_inicial:5.2f}")