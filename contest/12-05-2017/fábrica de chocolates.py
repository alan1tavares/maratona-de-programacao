def fabrica(entrada):
    entrada = list(map(int, entrada.split()))
    volumeParalelepipedo = entrada[0] * entrada[1] * entrada[2]
    return (int(pow(volumeParalelepipedo, 1/3)))

saida = ""
entrada_ = ""
while(True):
    entrada_ = input()
    if(entrada_ == "0 0 0"):
        break
    x = fabrica(entrada_)
    saida += str(x) + "\n"
print (saida[:len(saida)-1])
