import sys

for linha in sys.stdin:
    nParticipante, orcamento, nHoteis, nSemanas = map(int, linha.split())
    listaDeCusto = []
    for x in range(nHoteis):
        precoPorPessoa = int(sys.stdin.readline())
        semanaNCama = list(map(int, sys.stdin.readline().split()))

        custo = precoPorPessoa * nParticipante
        
        if custo < orcamento:
            for nCamas in semanaNCama:
                if nParticipante <= nCamas:
                    listaDeCusto.append(custo)
                    break

    if len(listaDeCusto) == 0:
        print('stay home')
    else:
        listaDeCusto = sorted(listaDeCusto)
        print(listaDeCusto[0])