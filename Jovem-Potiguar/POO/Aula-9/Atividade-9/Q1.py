
while True:
    try:
        num = int(input("Digite um número: "))
        dobro = num * 2
        print(f"O dobro desse número é: {dobro}")
        break

    except ValueError:
        print("ERRO!!! Digite um número")
    