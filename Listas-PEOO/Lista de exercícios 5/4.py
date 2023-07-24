str = input("Digite uma string: ").upper()

for i in range(len(str)):
    c = i - 1
    while c >= 0 and str[c] != str[i]:
        c -= 1
    if c < 0:
        count = str.count(str[i])
        print(f"A letra '{str[i]}' aparece {count} vezes na string.")