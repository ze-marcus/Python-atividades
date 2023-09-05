pag = float(input('Qual o valor a pagar? R$ '))
form = int(input('''
Qual a forma de pagamento? 
[ 1 ] Dinheiro/cheque 
[ 2 ] Cartão a vista
[ 3 ] Cartão 2x 
[ 4 ] Cartão 3x ou mais '''))
if form == 1:
    total = pag - (pag * 10 / 100)
    print('Total a pagar: R$ ', total)

elif form == 2:
    total = pag - (pag * 5 / 100)
    print('Total a pagar: R$ ', total)
elif form == 3:
    print('Total a pagar: R$ ', pag)
elif form == 4:
    total = pag + (pag * 20 / 100)
    print('Total a pagar: R$ ', total)