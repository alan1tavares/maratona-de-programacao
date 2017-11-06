import fileinput
for line in fileinput.input():
    line = int(line)
    if (line == 0):
        break
    soma = 0
    contador = 0
    while(contador < 5):
        if(line%2 == 0):
            contador+=1
            soma += line
        line+=1
    print(soma)