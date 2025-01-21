
while True:
    try:
        num = [10, 20, 30]
        select = int(input("Digite um índice da lista (0, 1, 2): "))
        print(f"{num[select]}")
        break

    except IndexError:
        print("ERRO!!! Este índice não existe")

    except ValueError:
        print("ERRO!!! Você precisa digitar um número")