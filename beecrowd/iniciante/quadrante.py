str_saida = ""
while True:
	int_coordenadas = list(map(int, input().split()))
	if ( int_coordenadas[0] == 0 or int_coordenadas[1] == 0 ):
		break
	if( int_coordenadas[0] > 0):
		if(int_coordenadas[1] > 0):
			str_saida += "primeiro\n"
		else:
			str_saida += "quarto\n"
	else:
		if(int_coordenadas[1] > 0):
			str_saida += "segundo\n"
		else:
			str_saida += "terceiro\n"
print( str_saida[:len(str_saida)-1] )