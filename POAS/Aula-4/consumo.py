import requests 

URL = "http://127.0.0.1:8000/"

def listar_livros():
    r = requests.get(f"{URL}/livros")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def listar_livros_titulo(titulo):
    r = requests.get(f"{URL}/livros/{titulo}")
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
    r = requests.post(f"{URL}/livros", json=livro)
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def excluir_livro(titulo):
    r = requests.delete(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def menu():
    print('1 - Listar livros')
    print('2 - Listar livros pelo título')
    print('3 - Cadastrar livro')
    print('4 - Deletar livro')
    print('5 - Sair')
    return int(input("Digite sua opção: "))

opcao = menu()

while opcao != 5:
    if opcao == 1:
        listar_livros()
    elif opcao == 2:
        titulo = str(input("Digite o título: "))
    elif opcao == 3:
        cadastrar_livro()
    elif opcao == 4:
        titulo = str(input("Digite o titulo: "))
        excluir_livro(titulo)
    
    opcao = menu()