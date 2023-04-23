import fileinput
# r1, x1, y1 - cacador
# r2, x2, y2 - flor de fogo
saida = ""
for linha in fileinput.input():
    if(linha == "\n"):
        break
    else:
        entrada = list(map(int, linha.split()))
        raioC = entrada[0]
        raioF = entrada[3]

        limiteEsquerda = abs(entrada[4] - raioF) <= abs(entrada[1] - raioC)
        #print (limiteEsquerda)
        limiteDireito  = raioC + entrada[1] >= raioF + entrada[4]
        #print (limiteDireito)
        
        limiteSuperior = entrada[5] + raioF <= entrada[3] + raioC
        #print(limiteSuperior)
        limiteInferior = abs(entrada[5] - raioF) <= abs(raioC - entrada[3])
        #print(limiteInferior)
        
        if(limiteSuperior and limiteInferior and limiteEsquerda and limiteDireito):
            saida += "RICO\n"
        else:
            saida += "MORTO\n"
print (saida[:len(saida)-1])
