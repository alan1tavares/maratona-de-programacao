f_entrada = list(map(int, input().split()))
a = 0
for i in range(1, max(f_entrada)):
	if(min(f_entrada) * i == max(f_entrada)):
		print("Sao Multiplos")
		a = 1
		break
if(a != 1):
	print("Nao sao Multiplos")