from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
jog = int(input('''Jokenpô!!!!!!!!!
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual a sua escolha? '''))

print('A maquina escolheu: {}'.format(itens[maquina]))
print('O jogador escolheu: {}'.format(itens[jog]))

if maquina == 0:
    if jog == 0:
        print('Empate!')
    elif jog == 1:
        print('Você ganhou!')
    elif jog == 2:
        print('Você perdeu!')

elif maquina == 1:
    if jog == 0:
        print('Você perdeu!')
    elif jog == 1:
        print('Empate!')
    elif jog == 2:
        print('Você ganhou!')

elif maquina == 2:
    if jog == 0:
        print('Você ganhou!')
    elif jog == 1:
        print('Você perdeu!')
    elif jog == 2:
        print('Empate!')