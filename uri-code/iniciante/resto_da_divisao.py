int_intervalo = [int(input()), int(input())]
int_v = [ n for n in range( min(int_intervalo)+1, max(int_intervalo) ) if( n%5==3 or n%5==2 )]
for c in int_v:
	print(c)