int_n = int(input())
int_count = 1
str_saida = ""
for c in range(0 , int_n):
	for j in range(1, 4):
		str_saida += str("%d " % int_count)
		int_count += 1
	str_saida += "PUM\n"
	int_count += 1
print( str_saida[:len( str_saida )-1] )