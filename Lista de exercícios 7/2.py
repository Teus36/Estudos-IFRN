aprovados = []
reprovados = []

print('=-' * 30)

while True:
    nome = input("Nome do aluno('pare' para parar): ")
    if nome == 'pare':
        break
    media = float(input("Média aluno (0 a 100): "))
    alunos = {
        'nome': nome,
        'media': media
    }
    if media >= 60:
        aprovados.append(alunos)
    else:
        reprovados.append(alunos)

print("=-" * 9 + " ALUNOS APROVADOS " + "=-" * 10)
for a in aprovados:
    print(f"ALUNO: {a['nome']} | MÉDIA: {a['media']}")

print("=-" * 9 + " ALUNOS REPROVADOS " + "=-" * 10)
for r in reprovados:
    print(f"ALUNO: {r['nome']} | MÉDIA: {r['media']}")
