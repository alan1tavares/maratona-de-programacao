# 1471
import fileinput

entrada = 0
for linha in fileinput.input():
    if(entrada == 0):
        mergulhou, retornou = list(map(int, linha.split()))
        entrada += 1
    else:
        entrada = 0

        morreu = list(range(1, mergulhou + 1))
        pessoasRetornaram = list(map(int, linha.split()))

        for x in pessoasRetornaram:
            morreu.remove(x)

        if(len(morreu) != 0):
            print(str(morreu).strip("[]").replace(",", "") + " ")
        else:
            print("*")
