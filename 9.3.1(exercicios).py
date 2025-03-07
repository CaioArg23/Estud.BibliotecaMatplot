#Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente. 
#lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

import random as rm
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
lista2 = rm.choice(lista)
print(lista2)