notas = {'1º Trimestre': 8.5, '2º Trimestre': 9.5, '3º Trimestre': 7}

def media():
    calculo = round(sum(notas.values())/len(notas.values()),1)
    print(calculo)

media()