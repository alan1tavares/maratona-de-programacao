def mochila(capacidade , peso , valo , n):
 
    if n == 0 or capacidade == 0 :
        return 0
 
    if (peso[n-1] > capacidade):
        return mochila(capacidade , peso , valor , n-1)
    else:
        return max(valor[n-1] + mochila(capacidade-peso[n-1] , peso , valor , n-1),
                   mochila(capacidade , peso , valor , n-1))

for galho in range(1, int(input())+1):
    num_pacotes = int(input())
    capacidade = int(input())
    valor = []
    peso = []
    for pacote in range(num_pacotes):
        v,p = map(int, input().split())
        valor.append(v)
        peso.append(p)
    print('Galho {}:'.format(galho))
    print('Numero total de enfeites: {}\n'.format(mochila(capacidade, peso, valor, num_pacotes)))

