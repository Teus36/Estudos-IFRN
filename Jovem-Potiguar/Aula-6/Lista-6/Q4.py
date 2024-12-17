numeros = [2, 7, 10, 15, 20, 33, 42]


def numero_par():
    print(f"Números pares:")
    for i in range(len(numeros)):
        if numeros[i]%2 == 0:
            print(numeros[i])
    
numero_par()