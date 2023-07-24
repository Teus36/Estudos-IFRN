meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

nasc = input("Digite sua data de nascimento: ")
dia, mes, ano = nasc.split('/')
mes_extenso = meses[int(mes)-1]

print(f"{dia} de {mes_extenso} de {ano}")