import fileinput


def isValida(tabuleiro, i, j):
    # print("%d, %d | %s\n"%(i,j, entrada[i][j:j+1]))

    # linha
    if(tabuleiro[i] [j+1 : 8].find('*') > 0):
        # print("caso2")
        return False

    # coluna
    for i2 in range(i+1, 8):
        # print("%d, %d | %s"%(i2,j, entrada[i2][j:j+1]))
        if (tabuleiro[i2][j:j+1] == '*'):
            # print("caso3")
            return False


    #diagonal direita
    for i2, j2 in zip(range(i+1, 8), range(j+1, 8)):
        # print("%d, %d | %s"%(i2,j2, entrada[i2][j2:j2+1]))
        if(entrada[i2][j2:j2+1] == '*'):
            # print("caso4")
            return False
    #giagonal
    for i2, j2 in zip(range(i+1, 8), reversed(range(0, j))):
        # print("%d, %d | %s"%(i2,j2, entrada[i2][j2:j2+1]))
        if(entrada[i2][j2:j2+1] == '*'):
            # print("caso5")
            return False
    return True




valido = True
entrada = []
count = 0;
for line in fileinput.input():
    entrada.append(line);
for i in range(0, len(entrada)):
    jRainha = entrada[i].find("*")
    if(jRainha > 0):
        if(not isValida(entrada, i, jRainha)):
            valido = False
            break
    else:
        count+=1

if(valido and count != len(entrada)):
    print("valid")
else:
    print("invalid")
