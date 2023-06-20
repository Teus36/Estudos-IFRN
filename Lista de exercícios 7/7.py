valor_apurado = litros_etanol = litros_gasolina = litros_diesel = 0.0
carros_atendidos = 0

print("***** Posto Mateus Batista ******")
print(f"  Valor Apurado no DIA: R$ {valor_apurado:.2f}")
print("*********************************")

while True:
    print("********* Registrar Abastecimento *********")
    placa = input("Digite a placa do veículo ou 0 para finalizar: ")
    if placa == '0':
        break

    combustivel = input("Combustível (etanol, gasolina ou diesel): ")
    litros = float(input("Quantidade de litros abastecida: "))

    if combustivel == 'etanol':
        valor_apurado += litros * 5.0
        litros_etanol += litros
    elif combustivel == 'gasolina':
        valor_apurado += litros * 6.0
        litros_gasolina += litros
    elif combustivel == 'diesel':
        valor_apurado += litros * 5.5
        litros_diesel += litros

    carros_atendidos += 1

print("***** Relatório de Abastecimentos *****")
print(f"Quantidade de carros atendidos: {carros_atendidos}")
print(f"Quantidade de litros de etanol vendidos: {litros_etanol}")
print(f"Quantidade de litros de gasolina vendidos: {litros_gasolina}")
print(f"Quantidade de litros de diesel vendidos: {litros_diesel}")
print(f"Total apurado no dia: R$ {valor_apurado:.2f}")