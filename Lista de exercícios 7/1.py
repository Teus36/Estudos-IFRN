agenda = []

for i in range(5):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    registros = {
        'nome': nome,
        'telefone': telefone
    }
    agenda.append(registros)

print("=-" * 9 + " REGISTROS DA AGENDA " + "=-" * 10)
for registros in agenda:
    print(f"Nome: {registros['nome']}, Telefone: {registros['telefone']}")
print("=-" * 30)