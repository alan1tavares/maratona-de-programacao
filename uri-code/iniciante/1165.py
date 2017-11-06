for x in range (0, int(input())):
    numero = int(input())
    contador = 0
    for y in range(1,numero+1):
        if(numero%y == 0):
            contador += 1
    if(contador > 2):
        print("%d nao eh primo" % (numero))
    else:
        print("%d eh primo" % (numero))