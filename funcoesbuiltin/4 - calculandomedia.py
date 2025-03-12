notas = {'1º Trimestre': 8.5, '2º Trimestre': 9.5, '3º Trimestre': 7}

calculo = sum(notas.values())/len(notas.values())
arredondado = round(calculo, 2)
print(arredondado)