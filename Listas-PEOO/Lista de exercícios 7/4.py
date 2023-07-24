consumo_feijao = {
    'Feijoada': 0.0,
    'Feijão Verde': 0.0
}

while True:
    print("*********** Consumo de Feijão na Cantina ***********")
    print("Foram consumidos até o momento aproximadamente:")
    print(f"* {consumo_feijao['Feijoada']:.2f} quilos de Feijoada")
    print(f"* {consumo_feijao['Feijão Verde']:.2f} quilos de Feijão Verde")
    print("****************************************************")
    print("Digite:")
    print("1 para registrar a venda de um prato de Feijoada")
    print("2 para registrar a venda de um prato de Feijão Verde")

    opcao = input("Opção: ")

    if opcao == '1':
        consumo_feijao['Feijoada'] += 0.20
    elif opcao == '2':
        consumo_feijao['Feijão Verde'] += 0.20
    else:
        break

print("*********** Consumo de Feijão na Cantina ***********")
print("Foram consumidos até o momento aproximadamente:")
print(f"* {consumo_feijao['Feijoada']:.2f} quilos de Feijoada")
print(f"* {consumo_feijao['Feijão Verde']:.2f} quilos de Feijão Verde")
print("****************************************************")