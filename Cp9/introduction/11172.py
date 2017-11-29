nCasosTeste = int(input())
for i in range(0, nCasosTeste):
    x, y = map(int, input().split())
    if(x == y):
        print('=')
    elif(x < y):
        print('<')
    else:
        print('>')
