import fileinput
def numerandoEstradas (entrada, caso):
    entrada = list(map(int, entrada.split()))
    r = entrada[0]
    n = entrada[1]

    numeroMinimoDeSufixos = 0
    restoRuas = r - n

    while(numeroMinimoDeSufixos < 26):
        if(restoRuas <= 0):
            break
        else:
            restoRuas -= n
        numeroMinimoDeSufixos += 1
    saida = ""
    if(r == 0):
        saida = "Case "+str(caso)+": impossible"
    elif(restoRuas > 0):
        saida = "Case "+str(caso)+": impossible"
    else:
        saida = "Case "+str(caso)+": " + str(numeroMinimoDeSufixos)
    return saida

saida_ = ""
caso_ = 1
n_linhas = 0
for linha in fileinput.input():
    n_linhas += 1
    
    string = linha.split()
    para = (len(string[0]) == 1 and len(string[1]) == 1) and (int(string[0]) == 0 and int(string[1]) == 0)
    if(n_linhas > 10002):
        break
    if (para):
        break
    else:
        saida_ += str(numerandoEstradas(linha, caso_)) + "\n"
    caso_ += 1
print (saida_[:len(saida_)-1])
