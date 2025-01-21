
class IdadeNegativa(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem

while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade > 0:
            print(f"Você tem {idade} anos")
            break
        else:
            raise IdadeNegativa("Idade inválida")

    except ValueError:
        print(f"Erro: Você precisa digitar um número")
    
    except IdadeNegativa as e:
        print(f"Erro: {e}")

