import fileinput
lista = []
for x in fileinput.input():
    h = int(x)
    for i in range(0, h):
        auxL = list(map(int, input().split()))
        lista.append(auxL)
    
    lista.sort()
    var = lista[0][0] + lista[0][1]
    for l in range(1, len(lista)):
        if(var < lista[l][0]):
            var = lista[l][0] + lista[l][1]
        else:
            var += lista[l][1]
    print(var)
    lista = []  