import math
angulo = float(input('digite o ângulo que voce deseja :'))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o SENO de {} '.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('o angulo de {} tem o COSSENO {}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem a TANGENTE de {}'.format(angulo, tangente))
