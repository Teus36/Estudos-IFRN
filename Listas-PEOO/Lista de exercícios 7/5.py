alunos = {}
aluno = []
cont = 0
soma_nota1 = soma_nota2 = 0

while True:
    matricula = int(input("Matricula('0' para parar): "))
    if matricula == 0:
        break
    aluno.append(input("Nome do aluno: "))
    aluno.append(float(input("Nota 1 (0 a 100): ")))
    aluno.append(float(input("Nota 2 (0 a 100): ")))
    alunos.update({matricula: aluno})
    aluno = []
    cont += 1

print("=-" * 40)
print(f"O número de alunos cadastrados foram: {cont}")
print(f"O nomes do alunos cadastrados são:", end=' ')
for aluno in alunos.values():
    print(f"{aluno[0]}", end=' ')
print(' ')
for aluno in alunos.values():
    soma_nota1 += aluno[1]
    soma_nota2 += aluno[2]
print(f"Média da 1ª Unidade: {soma_nota1 / cont}")
print(f"Média da 2ª Unidade: {soma_nota2 / cont}")
print(f"A Média final da turma foi: {((soma_nota1 + soma_nota2) / (len(alunos) * 2))}")
print(f"Lista de alunos aprovados: ")
for aluno in alunos.values():
    media_aluno = (aluno[1] + aluno[2]) / 2
    if media_aluno > 60:
        print(f" Nome: {aluno[0]}  |  Média: {media_aluno:.2f}")
