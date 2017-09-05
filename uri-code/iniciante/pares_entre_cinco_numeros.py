int_qtd_pares = 0
for c in range(0,5):
	int_entrada = int(input())
	if(int_entrada%2 == 0):
		int_qtd_pares += 1
print("%d valores pares" % int_qtd_pares)