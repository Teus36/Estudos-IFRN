valores = []

while True:
    user = int(input("Digite um número (para sair, digite -1): "))
    if user != -1:
        valores.append(user)
        print(f"Sua lista de valores está assim: {valores}")
    else:
        break
