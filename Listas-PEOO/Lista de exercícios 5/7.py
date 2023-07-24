frase = input("Digite uma frase: ").lower()
frase = frase.replace(" ", "")

if frase == frase[::-1]:
    print("Palíndromo")
else:
    print("Não é palíndromo")