while(True):
    numMeses, adiantamento, valEmprestimo, numDepre = map(float, input().split())
    if(numMeses < 0):
        break
    lista = list(range(0,101))
    prestacaoEmprestimo = valEmprestimo / numMeses
    valCarro = valEmprestimo + adiantamento

    for x in range(int(numDepre)):
        mes, valDepre = map(float, input().split())
        for y in range(int(mes), 100):
            lista[y] = valDepre

    for x in range(101):
        valCarro -= valCarro * lista[x]
        if(x!=0):
            valEmprestimo -= prestacaoEmprestimo
        if(valEmprestimo < valCarro):
            break

    if(x == 1):
        print("%d month" % x)
    else:
        print("%d months" % x)