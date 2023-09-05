tabuada = int(input("Tabuada de multiplicação do numero: "))

for soma in range(10):
    print("%a x %a = %a" % (tabuada, soma+1, tabuada*(soma+1)))

TabuadaDivisao = int(input("Tabuada de divisão do numero: "))

for div in range(10):
    print("%d / %d = %f" % (TabuadaDivisao, div+1, TabuadaDivisao/(div+1)))
