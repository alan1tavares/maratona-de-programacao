soma = count = 0
for c in range(0, 6):
	f_entrada = float(input())
	if(f_entrada > 0):
		count += 1
		soma += f_entrada
print("%d valores positivos" % count)
print("%.1f" % (soma/count))