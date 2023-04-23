numerDeCasos = int(input())
for x in range(0, numerDeCasos):
    numAssentos, numAmigos = list(map(int, input().split()))
    linhaAssentos = input()
    c = (numAmigos * "0") + "0"
    if(linhaAssentos.find(c) == -1):
        print("no")
    else:
        print("yes")
