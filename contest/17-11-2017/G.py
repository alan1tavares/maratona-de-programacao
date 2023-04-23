maiorPalavra = ""
while (True):
    palavra = input()
    saida = ""
    
    if(palavra == "0"):
        break
    palavra = palavra.split()
    
    for x in palavra:
        saida += str(len(x)) + "-"
        if(len(x) >= len(maiorPalavra)):
            maiorPalavra = x
    
    print(saida[:len(saida)-1])
print("\nThe biggest word: " + maiorPalavra)
