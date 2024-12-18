idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Você é criança")
elif 12 <= idade < 18: 
    print("Você é adolescente")
elif idade >= 18:
    print("Você é adulto")
    