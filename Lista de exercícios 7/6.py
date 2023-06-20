agenda = {}
contatos = []

while True:
    print("******** Agenda em Python *********")
    print("Existem:", len(agenda), "contatos cadastrados")
    print("***********************************")
    print("1. Inserir um contato")
    print("2. Consultar um contato")
    print("3. Remover um contato")
    print("4. Listar toda a agenda")
    print("0. Finalizar")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        break

    elif opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número de telefone do contato: ")
        email = input("Digite o email do contato: ")
        agenda[nome] = {'telefone': [telefone], 'email': [email]}

    elif opcao == 2:
        nome = input("Digite o nome do contato que deseja buscar: ")
        if nome in agenda:
            contato = agenda[nome]
            print("Nome:", nome)
            print("Telefone:", end=' ')
            for telefone in contato['telefone']:
                print(telefone)
            print("E-mail:", end=' ')
            for email in contato['email']:
                print(email)
        else:
            print("Contato não encontrado na agenda.")

    elif opcao == 3:
        nome = input("Digite o nome do contato: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado na agenda.")

    elif opcao == 4:
        print("***** Lista de Contatos *****")
        for nome, contato in agenda.items():
            print(f"Nome: {nome}")
            print(f"Telefone: ")
            for telefone in contato['telefone']:
                print(telefone)
            print("E-mail:")
            for email in contato['email']:
                print(email)
            print("*****************************")

    print(" ")




