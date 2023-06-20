frase = input("Digite uma frase: ")

frase = frase.replace(".", " ")
frase = frase.replace("!", " ")
frase = frase.replace("?", " ")
frase = frase.replace(",", " ")
frase = frase.replace(";", " ")
frase = frase.replace(":", " ")
palavras = frase.split()

print(f"O número de palavras da frase é : {len(palavras)}")
