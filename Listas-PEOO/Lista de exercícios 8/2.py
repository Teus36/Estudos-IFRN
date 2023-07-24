def main():
    while True:
        print("=-" * 30)
        string = str(input("Digite uma string qualquer: ")).strip().lower()

        if string == 'sair':
            break
        else:
            texto_codificado = simbolos(string)
            print(f"Texto codificado: {texto_codificado}")


def simbolos(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    simbolos = ['#', '@', '*', '$', '&']
    texto_codificado = ''

    for letra in string:
        if letra.lower() in vogais:
            indice = vogais.index(letra.lower())
            texto_codificado += simbolos[indice]
        else:
            texto_codificado += letra

    return texto_codificado


main()
