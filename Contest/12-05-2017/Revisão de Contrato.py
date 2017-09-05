import fileinput
def revisaoDeContrato(entrada):
    entrada = entrada.split()
    saida = ""
    for i in range(0, len(entrada[1])):
        saida = entrada[1].replace(entrada[0], "")
    if(saida == ""):
        return (0)
    else:
        saida = int(saida)
        return (saida)

saida_ = ""
for linha in fileinput.input():
    string = linha.split()
    para = (len(string[0]) == 1 and len(string[1]) == 1) and (int(string[0]) == 0 and int(string[1]) == 0)
    if (para):
        break
    else:
        saida_ += str(revisaoDeContrato(linha)) + "\n"
print (saida_[:len(saida_)-1])
