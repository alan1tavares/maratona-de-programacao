r, c = map(int, input().split())
mapa = []
linha = 0
coluna = 0
for i in range(r):
    mapa.append(input())
for i in range(r):
     if(mapa[i].find('S') < 0):
         linha += c
mapa = list(zip(*mapa))
for i in range(c):
    if((''.join(mapa[i]).find('S') < 0)):
        coluna += (r - linha//c)
print(linha+coluna)