int_qtd_pares = int_qtd_positivos = int_qtd_negativos = 0
for c in range(0,5):
	int_entrada = int(input())
	if(int_entrada%2 == 0):
		int_qtd_pares += 1
	if(int_entrada > 0):
		int_qtd_positivos += 1
	elif(int_entrada < 0):
		int_qtd_negativos +=1

print("%d valor(es) par(es)" % int_qtd_pares)
print("%d valor(es) impar(es)" % (5 - int_qtd_pares) )
print("%d valor(es) positivo(s)" % int_qtd_positivos)
print("%d valor(es) negativo(s)" % int_qtd_negativos)