str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

if str2 in str1:
    ind = str1.index(str2)
    print(f"A string 2 foi encontrada na 1, na posição: {ind}")
