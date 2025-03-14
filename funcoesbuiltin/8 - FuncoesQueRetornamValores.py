notas = [9.0, 8.0, 7.5, 7.0]

def media(lista):
    calculo = sum(lista) / len(lista)
    return calculo

resultado = media(notas)
print(resultado)