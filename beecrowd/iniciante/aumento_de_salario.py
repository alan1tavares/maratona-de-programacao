f_salario = float(input())
if(f_salario>=0 and f_salario<=400):
	f_percentual = 0.15
	f_reajuste = round(f_salario * f_percentual, 2)
elif(f_salario <= 800):
	f_percentual = 0.12
	f_reajuste = round(f_salario * f_percentual, 2)
elif(f_salario <= 1200):
	f_percentual = 0.1
	f_reajuste = round(f_salario * f_percentual, 2)
elif(f_salario <= 2000):
	f_percentual = 0.07
	f_reajuste = round(f_salario * f_percentual, 2)
else:
	f_percentual = 0.04
	f_reajuste = round(f_salario * f_percentual, 2)

print("Novo salario: %.2f" % round(f_reajuste+f_salario, 2))
print("Reajuste ganho: %.2f" % f_reajuste)
f_percentual = int(f_percentual * 100)
print("Em percentual: %d %%" % f_percentual)