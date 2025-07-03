import requests

url = "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{url}/livros")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def listar_livros_titulo(titulo):
    r = requests.get(f"{url}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def cadastrar_livro():
    titulo = input("Digite o título: ")
    ano = int(input("Digite o ano: "))
    edicao = int(input("Digite a edição: "))
    livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }
    r = requests.post(f"{url}/livros", json=livro)
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def excluir_livro(titulo):
    r = requests.delete(f"{url}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def editar_livro(titulo):
        r_get = requests.get(f"{url}/livros/{titulo}")
        if r_get.status_code == 200:
            novo_titulo = str(input("Digite um novo nome: "))
            novo_ano = int(input("Digite um novo ano: "))
            nova_edicao = int(input("Digite uma nova edição: "))
            livro_editado = {
                "titulo": novo_titulo,
                "ano": novo_ano,
                "edicao": nova_edicao
            }
            r_put = requests.put(f"{url}/livros/{titulo}", json=livro_editado)
            if r_put.status_code == 200:
                print(r_put.text)
            elif r_put.status_code == 404:
                print(r_put.text)
        elif r_get.status_code == 404:
            print(r_get.text)

def menu():
    print('=-'*9 + ' BIBLIOTECA ' + '=-'*9)
    print('( 1 ) - Listar livros')
    print('( 2 ) - Listar livros pelo título')
    print('( 3 ) - Cadastrar livro')
    print('( 4 ) - Deletar livro')
    print('( 5 ) - Editar livro')
    print('( 6 ) - Sair')
    print('=-'*24)
    return int(input("Digite sua opção: "))

if __name__ == "__main__":
    opcao = menu()

    while opcao != 6:
        if opcao == 1:
            listar_livros()
        elif opcao == 2:
            titulo = str(input("Digite o título: "))
        elif opcao == 3:
            cadastrar_livro()
        elif opcao == 4:
            titulo = str(input("Digite o titulo: "))
            excluir_livro(titulo)
        elif opcao == 5:
            titulo = str(input("Qual livro você quer editar ?: "))
            editar_livro(titulo)
    
        opcao = menu()
    
