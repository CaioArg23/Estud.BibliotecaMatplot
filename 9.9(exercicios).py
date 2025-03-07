#Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:
#numeros = [2, 8, 15, 23, 91, 112, 256]
from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

raiz = []

for numero in numeros:
  raiz.append(sqrt(numero))
 
for i in range(len(raiz)):
  
  if raiz[i] // 1 == raiz[i]:
    print(f"O número {numeros[i]} possui raiz quadrada inteira igual a {int(raiz[i])}")
