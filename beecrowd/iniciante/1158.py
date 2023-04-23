numeroDeCasos = int(input())
for x in range(0, numeroDeCasos):
    entrada = list(map(int, input().split()))
    contador = 0
    soma = 0
    while(contador < entrada[1]):
        if(entrada[0]%2 != 0):
            soma += entrada[0]
            # print (entrada[0])
            contador+=1
        entrada[0]+=1
    print(soma)