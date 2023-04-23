int_qtd_numeros = int(input())
int_in = 0
for c in range(0, int_qtd_numeros):
	int_val = int(input())
	if( int_val>=10 and int_val<=20 ):
		int_in += 1
print( "%d in" % int_in )
print( "%d out" % (int_qtd_numeros-int_in) )