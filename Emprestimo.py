val = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário ? '))
anos = int(input('Em quantos anos você terminara de pagar a casa? '))
prest = val / (sal * 12)
minimo = sal * 30 / 100
if prest <= minimo:
    print('Emprestimo aceito!')
else:
    print('Emprestimo negado!')