def decompor(valor, nota,moeda):
	n_notas = int(valor/nota)
	if(moeda!=0):
		if(nota == 1):
			print("{} moeda(s) de R$ {}.00".format(n_notas, nota))
		else:
			print("{} nota(s) de R$ {}.00".format(n_notas, nota))
	else:
		if(nota == 5 or nota == 1):
			print("{} moeda(s) de R$ 0.0{}".format(n_notas, nota))
		else:	
			print("{} moeda(s) de R$ 0.{}".format(n_notas, nota))

	return valor - n_notas*nota

dinheiro = round(float(input()), 2)
notas = int(dinheiro)
moedas = int((dinheiro-notas)*100)

print("NOTAS:")
dinheiro = decompor(dinheiro, 100, 1)
dinheiro = decompor(dinheiro, 50, 1)
dinheiro = decompor(dinheiro, 20, 1)
dinheiro = decompor(dinheiro, 10, 1)
dinheiro = decompor(dinheiro, 5, 1)
dinheiro = decompor(dinheiro, 2, 1)

print("MOEDAS:")
dinheiro = decompor(dinheiro, 1, 1)
moedas = decompor(moedas,50, 0)
moedas = decompor(moedas,25, 0)
moedas = decompor(moedas,10, 0)
moedas = decompor(moedas,5, 0)
moedas = decompor(moedas,1, 0)