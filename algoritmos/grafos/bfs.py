BRANCO = 1
CIZENTO = 2
corVertice = []
fila = []

numeroVertices = 8
grafo = [[] for x in range(numeroVertices)]


def adicionaVertice(vi, vf):
    grafo[vi].append(vf)

def bfs(vI):
    corVertice = [BRANCO] * numeroVertisces
    corVertice[vI] = CIZENTO
    fila.append(vI)

    while len(fila) < 0
        vU = 



