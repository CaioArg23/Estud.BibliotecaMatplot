#Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. 
#O token precisa ser par e variar de 1000 até 9998. 
# Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
#"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

from random import randint
numero = []
pergunta = str(input('digite o seu nome aqui: '))

numerominimo = 1000
numeromaximo = 9999
numero_aleatorio = randint(numerominimo, numeromaximo)

while numero_aleatorio % 2 == 1:
    numero_aleatorio = randint(numerominimo, numeromaximo)
    if numero_aleatorio % 2== 0:
        print(f'Olá, {pergunta}, o seu token de acesso é {numero_aleatorio}! Seja bem-vindo(a)')