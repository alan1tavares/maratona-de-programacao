# 2540

import fileinput

CONST = 2 / 3
primeira = 0
for linha in fileinput.input():
    if(primeira == 0):
        qtdJogadores = int(linha)
        primeira += 1
    else:
        primeira = 0
        somaVotos = sum(list(map(int, linha.split())))
        if(somaVotos / qtdJogadores >= CONST):
            print("impeachment")
        else:
            print("acusacao arquivada")
