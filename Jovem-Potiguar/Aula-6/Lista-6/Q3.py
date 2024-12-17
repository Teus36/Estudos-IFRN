
def tabuada(n1):
    for i in range(11):
        multi = n1 * i 
        print(f'{n1} * {i} = {multi}')

n = int(input("Digite um número: "))
tabuada(n)