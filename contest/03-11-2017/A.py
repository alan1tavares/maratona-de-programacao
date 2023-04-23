#2235
credito = list(map(int, input().split()))

resposta_S = (credito[0] == credito[1]) or (credito[0] == credito[2]) or (credito[1] == credito[2])
resposta_S = resposta_S or (credito[0]+credito[1] == credito[2]) or (credito[0]+credito[2] == credito[1]) or (credito[1]+credito[2]==credito[0])
resposta_S or (abs(credito[0]-credito[1]) == credito[2]) or (abs(credito[0]-credito[2]) == credito[1]) or (abs(credito[1]-credito[2])==credito[0])

if (resposta_S):
    print('S')
else:
    print('N')