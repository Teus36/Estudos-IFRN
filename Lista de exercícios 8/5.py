from datetime import datetime


def main():
    data_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")
    idade = (datetime.now() - data_nascimento).days // 365
    print(f"Você tem {idade} anos")


main()