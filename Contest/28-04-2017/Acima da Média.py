c = int(input())
saida = ""
for i in range(c):
    contador = 0
    n = list(map(int, input().split()))
    media = float((sum(n) - n[0])/n[0])
    for j in range(1, n[0]+1):
        if(float(n[j]) > media):
            contador += 1
    percentual = float((100*contador) / n[0])
    saida += ("%.3f%%\n" % percentual) 
print (saida[0:len(saida)-1])
