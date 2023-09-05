ano = int(input('Qual ano voce nasceu ? '))
idade = 2023 - ano

if idade < 18:
       print('Você não tem idade sufisciente para se alistar!')

elif idade == 18:
       print('Você tem que se alistar!')

elif idade > 18:
       print('Você ja passou da idade de se alistar')
