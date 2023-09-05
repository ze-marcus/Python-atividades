num = int(input('Digite um número: '))
esc = int(input('''===================================
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL
===================================
Escolha uma forma para conversão: '''))
if esc == 1:
    print('O numero BINÁRIO é: ', bin(num)[2:])
elif esc == 2:
    print('O numero OCTAL é: ', oct(num)[2:])
elif esc == 3:
    print('O numero HEXADECIMAL é: ', hex(num)[2:])
else:
    print('Opção invalida!')