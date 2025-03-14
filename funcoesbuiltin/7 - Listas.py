notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
    calculo = round(sum(lista) / len(lista),1)
    print(calculo)

media(notas)