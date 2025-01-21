import math

while True:
    try: 
        num1 = int(input("Digite um primeiro número: "))
        num2 = int(input("Digite um segundo número: "))
        multi = num1 * num2 
        raiz = math.sqrt(multi)
        print(raiz)
        break

    except ValueError:
        print(f"Erro: Você precisa digitar um número")
    
    