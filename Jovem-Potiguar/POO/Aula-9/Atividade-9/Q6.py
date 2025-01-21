
while True:
    try:
        frutas = ["maçã", "banana", "laranja"]
        select = int(input("Digite o índice de uma fruta que deseja remover (0, 1 ,2): "))
        remover = frutas.pop(select)
        print(frutas)
        break

    except IndexError:
        print("Erro: este índice não existe")

    except ValueError:
        print(f"Erro: Você precisa digitar um número")