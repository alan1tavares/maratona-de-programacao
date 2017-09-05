f_salario = float(input())
if(f_salario >= 0 and f_salario <= 2000.00):
	print("Isento")
elif(f_salario <= 3000.00):
	print("R$ %.2f" % ((f_salario-2000)*0.08))
elif(f_salario <= 4500):
	#1000 * 0.08 + (salario - 3000) * 0.18
	print("R$ %.2f" % (80 + (f_salario-3000) * 0.18))
elif(f_salario > 4500):
	#1000*0.08 + 1500*0.18 + ( salario-4500)*0.28
	print("R$ %.2f" % (80 + 270 + (f_salario-4500)*0.28))