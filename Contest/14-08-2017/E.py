numerDeCasos = int(input())
for x in range(0, numerDeCasos):
    numeroDeLivros = int(input())
    numeroDeEstantes = numeroDeLivros//5
    if(numeroDeLivros%5 != 0): numeroDeEstantes+=1
    print(numeroDeEstantes)
