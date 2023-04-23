dia_inicio = int(input().split()[1])
tempo_inicio = list(map(int, input().split(" : ")))
dia_final = int(input().split()[1])
tempo_final= list(map(int, input().split(" : ")))

tempo_inicio_segundos = (86400 * dia_inicio) + (3600*tempo_inicio[0]) + (60*tempo_inicio[1]) + tempo_inicio[2]
tempo_final_segundos = (86400 * dia_final) + (3600*tempo_final[0]) + (60*tempo_final[1]) + tempo_final[2]

delta_tempo = tempo_final_segundos - tempo_inicio_segundos

hora = int(delta_tempo/3600)
dia = int(delta_tempo/86400)
if(hora >= 24):
	hora -= 24*dia
print("%d dia(s)" % dia)
print("%d hora(s)" % hora)
print("%d minuto(s)" % ((int(delta_tempo/60)%60)))
print("%d segundo(s)" % (delta_tempo%60))