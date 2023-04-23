str_saida = ""
while(True):
	int_mn = list(map(int, input().split()))
	if(int_mn[0] <= 0 or int_mn[1] <= 0):
		break
	int_lista = range(min(int_mn), max(int_mn)+1)
	str_saida += "%s Sum=%d\n" % ( str(list(int_lista)).replace("[", "").replace("]", "").replace(",", ""), sum(int_lista) )
print(str_saida[:len(str_saida)-1])