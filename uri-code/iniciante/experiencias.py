int_n = int(input())
vint = [0,0,0]
for c in range(0 , int_n):
	entrada = input().split()
	if(entrada[1] == "C"):
		vint[0] += int(entrada[0])
	elif(entrada[1] == "R"):
		vint[1] += int(entrada[0])
	elif(entrada[1] == "S"):
		vint[2] += int(entrada[0])
soma = sum(vint)
print("Total: %d cobaias" % soma)
print("Total de coelhos: %d" % vint[0])
print("Total de ratos: %d" % vint[1])
print("Total de sapos: %d" % vint[2])
float_porcentagem = 100*vint[0] / soma
print("Percentual de coelhos: %.2f %%" % float_porcentagem )
float_porcentagem = 100*vint[1] / soma
print("Percentual de ratos: %.2f %%" %   float_porcentagem )
float_porcentagem = 100*vint[2] / soma
print("Percentual de sapos: %.2f %%" %   float_porcentagem )