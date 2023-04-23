# 2106

qtdJogadores = int(input())
saida = ""
while qtdJogadores != 0:
    menorCusto = sum(list(map(int, input().split())))

    for x in range(1, qtdJogadores):
        custoTotal = sum(list(map(int, input().split())))
        if(menorCusto > custoTotal): menorCusto = custoTotal
    
    qtdJogadores = int(input())
    saida += str(menorCusto) + "\n"
print(saida)

#Não passa