i_entrada = list(map(int, input().split()))
if(i_entrada[0] == i_entrada[2] and i_entrada[1] == i_entrada[3]):
	print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
	horas = i_entrada[0]-i_entrada[2]
	if(horas<0):
		horas = abs(horas)
	else:
		horas = 24 - i_entrada[0]
		horas += i_entrada[2]
	minutos = i_entrada[1]-i_entrada[3]
	if(minutos < 0):
		minutos = abs(minutos)
	else:
		horas -= 1
		minutos = 60 - minutos
	print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (horas, minutos))