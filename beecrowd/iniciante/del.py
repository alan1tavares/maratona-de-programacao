import fileinput
int_ls = []
for linha in fileinput.input():
	if(int(linha) == 0):
		break
	int_ls.append( range(1, int(linha)+1) )
for x in int_ls:
	print( str(x).replace(",", "").replace("[", "").replace("]", "") ) 



int_ls = []
while True:
	int_var = int(input())
	if( int_var == 0 ):
		break;
	int_ls.append( range(1, int_var+1) )
for x in range( 0, len(int_ls) ):
	print( str(int_ls[x]).replace(", ", " ").replace("[", "").replace("]", "") )