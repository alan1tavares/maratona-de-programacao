int_num = int(input())
str_saida = ""
for c in range(0, int_num):
	int_val = int(input())
	if ( int_val == 0 ):
		print("NULL")
	else:
		if( int_val%2 == 0 ):
			str_saida += "EVEN"
		else:
			str_saida += "ODD"
		if ( int_val > 0 ):
			str_saida += " POSITIVE"
		else:
			str_saida += " NEGATIVE"
		print(str_saida)
	str_saida = ""