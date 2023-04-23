import fileinput
distancia, sorveteiros = map(int, input().split())
testCase = 1
intervalos = []
while (distancia != 0 and sorveteiros != 0):
    for s in range(0, sorveteiros):
        dIncicio, dFim = map(int, input().split())
        if(dFim < distancia):
