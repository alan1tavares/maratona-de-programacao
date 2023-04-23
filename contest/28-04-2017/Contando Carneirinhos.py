t = int(input())
saida = ""
for i in range(t):
    n = int(input())
    carneiros = list(map(int, input().split()))
    carneiros.sort()
    caneirosUnicos = list(set(carneiros))
    saida += str(len(caneirosUnicos))+"\n"
print(saida[0:len(saida)-1])
