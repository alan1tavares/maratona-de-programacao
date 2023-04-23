i_entrada = list(map(int, input().split()))
if(i_entrada[0] == i_entrada[1]):
	print("O JOGO DUROU 24 HORA(S)")
else:
	horas = i_entrada[0]-i_entrada[1]
	if(horas<0):
		print("O JOGO DUROU %d HORA(S)" % abs(horas))
	else:
		horas = 24 - i_entrada[0]
		horas += i_entrada[1]
		print("O JOGO DUROU %d HORA(S)" % horas)