def data_por_extenso(data):
    meses = {
        "01": "JANEIRO", "02": "FEVEREIRO", "03": "MARÇO", "04": "ABRIL", "05": "MAIO", "06": "JUNHO",
        "07": "JULHO", "08": "AGOSTO", "09": "SETEMBRO", "10": "OUTUBRO", "11": "NOVEMBRO", "12": "DEZEMBRO"
    }
    numeros = {
        "01": "UM", "02": "DOIS", "03": "TRÊS", "04": "QUATRO", "05": "CINCO", "06": "SEIS", "07": "SETE",
        "08": "OITO", "09": "NOVE", "10": "DEZ", "11": "ONZE", "12": "DOZE", "13": "TREZE", "14": "QUATORZE",
        "15": "QUINZE", "16": "DEZESSEIS", "17": "DEZESSETE", "18": "DEZOITO", "19": "DEZENOVE", "20": "VINTE",
        "21": "VINTE E UM", "22": "VINTE E DOIS", "23": "VINTE E TRÊS", "24": "VINTE E QUATRO",
        "25": "VINTE E CINCO", "26": "VINTE E SEIS", "27": "VINTE E SETE", "28": "VINTE E OITO",
        "29": "VINTE E NOVE", "30": "TRINTA", "31": "TRINTA E UM"
    }

    dia, mes = data.split("/")
    dia = numeros[dia]
    mes = meses[mes]

    return f"{dia} DE {mes}"


def main():
    data = input("Digite uma data (DD/MM): ")
    data_extenso = data_por_extenso(data)
    print(data_extenso)


main()