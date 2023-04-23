f_lado = list(map(float, input().split()))
f_lado.sort()
f_lado.reverse()
if(f_lado[0] >= f_lado[1]+f_lado[2]):
	print("NAO FORMA TRIANGULO")
else:
	if(f_lado[0]**2 == f_lado[1]**2 + f_lado[2]**2):
		print("TRIANGULO RETANGULO")
	if(f_lado[0]**2 > f_lado[1]**2 + f_lado[2]**2):
		print("TRIANGULO OBTUSANGULO")
	if(f_lado[0]**2 < f_lado[1]**2 + f_lado[2]**2):
		print("TRIANGULO ACUTANGULO")
	if(f_lado[0]==f_lado[1] and f_lado[1]==f_lado[2]):
		print("TRIANGULO EQUILATERO")
	elif(f_lado[0]==f_lado[1] or f_lado[1]==f_lado[2] or f_lado[0] == f_lado[1]):
		print("TRIANGULO ISOSCELES")