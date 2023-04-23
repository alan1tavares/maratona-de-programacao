# casosDeTeste = int(input())
# for x in range(0 casosDeTeste):
#     tamanhoTrem = int(input())
vetor = list(map(int, input(split())))
print(str(ordenacao(vetor)))

def ordenacao(vetor):
    trocas = 0
    trocou = True
    while(trocou):
        trocou = False
        for i in range(0, len(vetor)-2):
            if(vetor[i] > vetor[i+1]):
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                trocas += 1
                trocou = True
    print(vetor)
    return trocas