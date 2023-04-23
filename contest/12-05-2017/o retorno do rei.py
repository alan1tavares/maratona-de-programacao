entrada = input()
string = entrada.replace("10", "x")
soma = 0
for i in range (0, len(string)):
    if (string[i] == "x"):
        soma += 10.0
    else:
        soma += float(string[i])
media = soma/len(string)
print ("%.2f" % media)
