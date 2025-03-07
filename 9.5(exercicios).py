#Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.
#Dica: use a função pow() da biblioteca math

from math import pow

n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))

resultado = pow(n1, n2)
print(f'{n1} elevado a {n2} é: {resultado}')