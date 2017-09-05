v_combustivel = [0, 0, 0,]
while True:
	int_opt = int(input())
	if( int_opt == 4 ):
		break
	elif( int_opt == 1 ):
		v_combustivel[0] += 1
	elif( int_opt == 2 ):
		v_combustivel[1] += 1
	elif( int_opt == 3 ):
		v_combustivel[2] += 1
print( "MUITO OBRIGADO" )
print( "Alcool: %d" % v_combustivel[0] )
print( "Gasolina: %d" % v_combustivel[1] )
print( "Diesel: %d" % v_combustivel[2] )