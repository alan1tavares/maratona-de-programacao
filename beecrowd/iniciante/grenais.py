int_grenais = 0
dint_resultado = {"inter" : 0, "gremio" : 0, "empates" : 0}
while True:
	int_val = list(map(int, input().split()))
	int_grenais += 1
	if( int_val[0] == int_val[1] ):
		dint_resultado["empates"] += 1
	elif ( int_val[0] > int_val[1] ):
		dint_resultado["inter"] += 1
	else:
		dint_resultado["gremio"] += 1
	print("Novo grenal (1-sim 2-nao)")
	int_op = int(input())
	if( int_op == 1):
		continue
	if ( int_op == 2):
		break
print( "%d grenais" % int_grenais )
print( "Inter:%d" % dint_resultado["inter"] )
print( "Gremio:%d" % dint_resultado["gremio"])
print( "Empates:%d" % dint_resultado["empates"])
if(dint_resultado["inter"] == dint_resultado["gremio"]):
	print("Nao houve vencedor")
elif(dint_resultado["inter"] > dint_resultado["gremio"]):
	print("Inter venceu mais")
else:
	print("Gremio venceu mais")