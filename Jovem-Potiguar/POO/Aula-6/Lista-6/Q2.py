numeros = [5, 8, 12, 20, 3]

def soma():
    soma = 0
    for i in range(0, len(numeros)):
        soma = soma + numeros[i]
    
    print(soma)

soma()