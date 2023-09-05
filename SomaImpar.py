mn = int(input('Qual seu número inicial? '))
mm = int(input('Qual seu número final? '))
soma = 0

print('=================================')

for impar in range(mn, mm+1):
    print(impar)
    if impar % 2 != 0:
        soma += impar

print('=================================')

print('A soma dos números ímpares é ', soma)