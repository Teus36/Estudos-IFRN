print("=-" * 30)

nome = str(input("Nome: "))
while len(nome) <= 3:
    print("ERRO!!! O NOME DEVE CONTER 3 OU MAIS CARACTÉRES")
    nome = str(input("Nome: "))

idade = int(input("Idade: "))
while idade > 100 or idade < 10:
    print("ERRO!!! A IDADE DEVE SER ENTRE 10 E 100")
    idade = int(input("Idade: "))

estado_c = str(input("Estado Civil: "))
while estado_c != "S" and estado_c != "C" and estado_c != "V" and estado_c != "D":
    print("ERRO!!! VOCÊ DEVE RESPONDER SOMENTE COM S,C,V OU D")
    estado_c = str(input("Estado Civil: "))

telefone = input("Telefone: ")
while len(telefone) != 9:
    print("ERRO!!! SEU NÚMERO DE TELEFONE DEVE CONTER 9 DIGITOS")
    telefone = input("Telefone: ")

print("=-" * 30)
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Estado Cívil: {estado_c} ")
print(f"Telefone: {telefone}")
print("=-" * 30)







