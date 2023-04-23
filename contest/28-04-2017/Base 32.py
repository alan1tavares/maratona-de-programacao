def base32(n):
    a_v = "A B C D E F G H I J K L M N O P Q R S T U V".split()
    #n = int(input())
    listaResto = list()
    auxResto = n%32
    auxQuociente = n//32
    listaResto.append(auxResto)
    while (True):
        if(auxQuociente >= 32):
            auxResto = auxQuociente%32
            auxQuociente = auxQuociente//32
            listaResto.append(auxResto)
        else:
            listaResto.append(auxQuociente)
            break
    listaResto.reverse()
    saida = ""
    for i in range(len(listaResto)):
        if(listaResto[i] < 10):
            saida += str(listaResto[i])
        elif(listaResto[i] < 32):
            saida += a_v[listaResto[i]-10]
    if(listaResto[0] == 0):
        return(saida[1:])
    else:
        return(saida)

saida = ""
while(True):
    n = int(input())
    saida += base32(n)+"\n"
    if(n==0):
        break
print(saida[:len(saida)-1])
