palavras = ["batata", "potato", "kartoffel", "patata", "bulvė"]
contador = 0
palavras_cinco = 0

while contador < len(palavras):
    if len(palavras[contador]) > 5:
        palavras_cinco += 1
    contador += 1

print(f"A lista contém {palavras_cinco} palavras com mais de 5 letras")