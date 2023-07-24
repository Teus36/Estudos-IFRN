from random import randint


def gerar_senha(tamanho_senha):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    tam_caract = len(caracteres)
    senha = " "

    for i in range(tamanho_senha):
        indice = randint(0, tam_caract - 1)
        senha += caracteres[indice]
    return senha


def main():
    tamanho_senha = int(input("Digite quantos caractéres terá sua senha: "))
    qt_senhas = int(input("Quantas senhas você quer gerar: "))

    arquivo = open('senhas.txt', 'w')
    for i in range(qt_senhas):
        senha = gerar_senha(tamanho_senha)
        arquivo.write(senha + "\n")

    arquivo.close()


main()