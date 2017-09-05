numeroTeste = int(input())
for x in range(0, numeroTeste):
    lista = list(map(int, input().split()));
    if (lista[0] >= lista[1]):
        print("FunkyMonkeys")
    else:
        print("WeWillEatYou")
