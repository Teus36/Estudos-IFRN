
def somar(a:int, b:int):
    return a+b

def subtrair(a:int, b:int):
    return a-b

def multiplicar(a:int, b:int):
    return a*b

def dividir(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        return "Não é possível realizar uma divisão por 0"
