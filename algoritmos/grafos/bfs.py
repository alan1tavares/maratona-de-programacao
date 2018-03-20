import fileinput

def adicionaVertice(vi, vf):
    grafo[vi].append(vf)

def bfs(vI):
    global numeroVertices
    global corVertice
    global BRANCO
    global CIZENTO
    global PRETO

    corVertice = [BRANCO] * numeroVertices
    distancia = [0] * numeroVertices
    corVertice[vI] = CIZENTO
    fila.append(vI)

    while len(fila) != 0:
        print(fila)
        vU = fila.pop(0)
        for vV in grafo[vU]:
            if corVertice[vV] == BRANCO:
                corVertice[vV] = CIZENTO
                distancia[vV] = distancia[vU] + 1
                # u.pi = u
                fila.append(vV)
        corVertice[vU] = PRETO

BRANCO = 1
CIZENTO = 2
PRETO = 3
corVertice = []
fila = []

numeroVertices = 8
grafo = [[] for x in range(numeroVertices)]

for line in fileinput.input():
    u,v = map(int, line.split())
    adicionaVertice(u, v)
print(grafo)
bfs(1)

