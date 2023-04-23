str_saida = ""
while(True):
	int_xy = list(map(int, input().split()))
	if(int_xy[0] == int_xy[1]): break
	if(int_xy[0] > int_xy [1]):
		str_saida += "Decrescente\n"
	else:
		str_saida += "Crescente\n"
print(str_saida[:len(str_saida)-1])