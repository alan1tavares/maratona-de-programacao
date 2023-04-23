int_var = list(map(int, list(input().split())))
str_saida = ""
for x in range(1, int_var[1]+1):
	str_saida += str(x) + " "
	if(x % int_var[0] == 0):
		print(str_saida[:len(str_saida)-1])
		str_saida = ""