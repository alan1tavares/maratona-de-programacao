int_n = int(input())
str_saida = ""
for c in range(0, int_n):
	float_entrada = list(map(float, input().split()))
	try:
		float_divisao = float_entrada[0]/float_entrada[1]
		str_saida += str("%.1f\n" % float_divisao)
	except ZeroDivisionError:
		str_saida += "divisao impossivel\n"
print( str_saida[:len(str_saida)-1] )