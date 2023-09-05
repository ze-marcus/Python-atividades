mn = int(input('Qual seu número inicial? '))
mm = int(input('Qual seu número final? '))
cont = 0

print('=================================')

for par in range(mn, mm+1):
    print(par)
    if par % 2 == 0:
        cont += 1

print('=================================')

print('O número de pares é ', cont)


