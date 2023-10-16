import requests, json 

cep = str(input("Digite o seu CEP: "))
consulta = requests.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")

resposta = consulta 

if resposta.status_code != 200:
    print("CEP inválido")
else:
    print(f"Rua: {consulta.json()['street']}")

