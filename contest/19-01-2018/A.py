dicionario = {}
n = int(input())
saida = ''

while n:
    for x in range(n):
        caso = input()
        if(caso[0] in dicionario):
            saida = 'Conjunto Ruim'
        else:
            dicionario[caso[0]] = 1
        
    if(saida != ''):
        print(saida)
    else:
        print('Conjunto Bom')

    n = int(input())
    saida = ''
    dicionario = {}