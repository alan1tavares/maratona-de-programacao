int_intervalo = [int(input()), int(input())]
int_v = [ n for n in range( min(int_intervalo), max(int_intervalo)+1 ) if( n%13 != 0 )]
print(sum(int_v))