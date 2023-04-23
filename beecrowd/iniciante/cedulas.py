def decompor(valor, nota):
	n_notas = 0
	if(valor/nota > 0):
		n_notas = int(valor/nota)
	print("{} nota(s) de R$ {},00".format(n_notas, nota))

	return valor - n_notas*nota

valor = int(input())
print(valor)
valor = decompor(valor, 100)
valor = decompor(valor, 50)
valor = decompor(valor, 20)
valor = decompor(valor, 10)
valor = decompor(valor, 5)
valor = decompor(valor, 2)
decompor(valor, 1)