tamanhDoVetor = int(input())
entrada_v = list(map(int, input().split()))
menor = entrada_v[0];
p = 0;
for x in range(1, tamanhDoVetor):
    if (entrada_v[x] < menor):
        menor = entrada_v[x]
        p = x
print ("Menor valor: %d" % (menor))
print ("Posicao: %d" % (p))
