import random

print('Eu irei escolher um número de 1 a 5 e você terá que acertar!')
numero = random.randint(1,5)
adivinhar = 0

while adivinhar != numero:

    adivinhar = int(input('Adivinhe o número: '))

    if(adivinhar == numero):
       print('Você ganhou!')
    elif (adivinhar != numero):
        print('Você errou, o número era ', numero)
        exit()
