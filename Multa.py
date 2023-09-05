vel = int (input('digite a velocidade do veiculo: '))
multa = (vel - 80) * 7.00
if vel<80:
    print('velocidade permitida')
else:
    print('Você ultrapassou o limite de velocidade e foi multado em R$', multa)
