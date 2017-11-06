casosDeTeste = int(input())
for x in range (0, casosDeTeste):
    pa, pb, g1, g2 = list(map(float, input().split()))
    contador = 0
    while(contador < 102):
        pa += int((g1/100)*pa)
        pb += int((g2/100)*pb)
        contador += 1
        if(pa > pb):
            break
    if(contador > 100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % (contador))