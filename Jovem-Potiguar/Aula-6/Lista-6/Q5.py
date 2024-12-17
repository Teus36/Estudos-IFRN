notas = [7.5, 8.0, 6.5, 9.0, 7.0]

def media_notas():
    soma = 0
    for i in range(len(notas)):
        soma = soma + notas[i]
    
    media = soma/len(notas)
    print(f"A média das notas é: {media}")

media_notas()