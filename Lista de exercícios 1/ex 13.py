val_com = float(input("Informe o valor das compras: "))
desconto = val_com - val_com * 3/100
print(f"O valor das suas compras foram R${val_com}")
print(f"Se pagar no PIX será R$ {desconto}")
print(f"O valor do desconto é de R$ {val_com - desconto}")
