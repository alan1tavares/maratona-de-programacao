f_entrada = float(input())
if(f_entrada < 0):
	print("Fora de intervalo")
elif(f_entrada <= 25):
	print("Intervalo [0,25]")
elif(f_entrada <= 50):
	print("Intervalo (25,50]")
elif(f_entrada <= 100):
	print("Intervalo (75,100]")
else:
	print("Fora de intervalo")