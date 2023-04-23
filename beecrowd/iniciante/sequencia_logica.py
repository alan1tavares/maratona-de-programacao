int_n = int(input())
str_saida = ""
for c in range(1, int_n+1):
	print( "%d %d %d" % (c, c**2, c**3))
	print( "%d %d %d" % (c, c**2+1, c**3+1))