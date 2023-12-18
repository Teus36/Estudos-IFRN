numeros = []

while True:
    try:
      num1 = int(input('Digite um número: '))
      num2 = int(input('Digite um segundo número: '))
    except ValueError as erro:
      print(f'Foi encontrado o erro de "{erro}"')
      print(f"Do tipo {type(erro)}")
    else:
       numeros.append(num1)
       numeros.append(num2)
       break

print(numeros)