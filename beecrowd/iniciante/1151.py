n = int(input())
if n == 0:
    print()
proximoNumero = 1
lista = [0, 1]
saida = ""
for x in range(0, n):
    if x == 0:
        saida += "0 "
    elif x == 1:
        saida += "1 "
    else:
        lista.append(lista[x-2]+lista[x-1])

print (str(lista).strip("[]").replace(",", ""))
