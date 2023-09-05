n1 = float(input('Nota da prova: '))
n2 = float(input('Nota do trabalho: '))

media = (n1 + n2) / 2
print('Sua média é: ', media)
if media < 60:
    print('Você reprovou!')
elif 70 > media >= 60:
    print('Você esta em recuperação!')
elif media >= 70:
    print('Você está aprovado!')