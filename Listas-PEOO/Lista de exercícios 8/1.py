def menu():
    while True:

        print("=-" * 7 + " AGENDA " + "=-" * 7)
        print("[ 1 ] Adicionar registro")
        print("[ 2 ] Apagar registro")
        print("[ 3 ] Listar amigos")
        print("[ 4 ] Sair")
        opcao = input("Digite a opção desejada: ")
        print("=-" * 18)
        if opcao == "1":
            adicionar_registro()
        elif opcao == "2":
            apagar_registro()
        elif opcao == "3":
            listar_amigos()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")


def adicionar_registro():
    CPF = str(input("CPF: "))
    nome = str(input("Nome: "))
    telefone = str(input("Telefone: "))

    arquivo = open("agenda.txt", "a")
    arquivo.write(f"{CPF},{nome},{telefone}\n")
    arquivo.close()
    print("REGISTRO ADICIONADO!")


def apagar_registro():
    CPF = str(input("Digite qual CPF você quer apagar: "))

    arquivo = open("agenda.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    arquivo = open("agenda.txt", "w")
    for linha in linhas:
        dados = linha.strip().split(",")
        if dados[0] != CPF:
            arquivo.write(linha)
    arquivo.close()
    print("REGISTRO APAGADO!")


def listar_amigos():
    arquivo = open("agenda.txt", "r")
    registros = arquivo.readlines()

    if registros:
        print("=-" * 10 + " REGISTROS NA AGENDA " + "=-" * 9)
        for registro in registros:
            dados = registro.strip().split(",")
            print(f"CPF: {dados[0]} | Nome: {dados[1]} | Telefone: {dados[2]}")
    else:
        print("Agenda vazia!")



menu()
