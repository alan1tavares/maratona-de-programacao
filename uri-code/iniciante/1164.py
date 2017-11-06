for j in range(0, int(input())):
    x = int(input())
    somatorio = 0
    for i in range(1, x):
        if(x%i==0):
            somatorio += i
    if(somatorio == x):
        print("%d eh perfeito" %(x))
    else:
        print("%d nao eh perfeito" % (x))