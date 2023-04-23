import fileinput
def sanduiche(entrada):
    saida = ""
    h=1
    
    for j in reversed(range(len(entrada))):
        aux = entrada[j:]
        
        if(entrada[:len(entrada)-h].find(aux) < 0 or len(entrada) < 2):
            aux2 = entrada[j+1:]
            atringQueEuACheiTaNoComeco = (entrada[:len(entrada) - len(aux2)].find(aux2)) == 0 and len(aux2)*2 != len (entrada)

            if(entrada.replace(entrada[0], "") == "" and len (entrada)>1):
                return (entrada[:len(entrada)-1])

            if(atringQueEuACheiTaNoComeco):
                return (entrada)
            saida = entrada[:j+1]
            break
        h+=1
    return (saida)


entrada_eof=""
for linha in fileinput.input():
    if (linha == "\n"):
        break
    entrada_eof += linha
entrada_eof = entrada_eof.split("\n")
saida2 = ""
for i in range(len(entrada_eof)):
    saida2 += sanduiche(entrada_eof[i])+"\n"
print(saida2[:len(saida2)-2])
