int_n = int(input())
saida = ""
for c in range(0, int_n):
	vfloat_notas = list(map(float, input().split()))
	media = ( (vfloat_notas[0]*2) + (vfloat_notas[1]*3) + (vfloat_notas[2]*5)) / 10
	if ( c == int_n-1 ):
		saida += str("%.1f" % media)
	else:
		saida += str("%.1f" % media) + "\n"
print(saida)