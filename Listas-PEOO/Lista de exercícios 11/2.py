try:
  x = int(input('Digite um Número: '))
  y = int(input('Digite outro Número: '))
  print(x/y)
except Exception as erro:
  print(f'Erro Encontrado = {erro} ')
  print(f'Tipo/Classe do Erro Encontrado = {type(erro)} ')