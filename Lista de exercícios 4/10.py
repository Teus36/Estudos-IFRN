l = []
n = ""
n_final = ""
while n != 0:
    n = int(input("Digite um número: "))
    l.append(n)
    
for i in range(0, len(l)):
    n_final += str(l[i])

print(n_final)