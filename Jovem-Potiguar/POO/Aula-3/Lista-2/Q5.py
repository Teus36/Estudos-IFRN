peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso/(altura**2)

if imc < 18.5:
    print("Você está abaixo do peso")
elif 18.5 < imc < 25: 
    print("Seu peso está normal")
elif imc > 25:
    print("Você está acima do peso")