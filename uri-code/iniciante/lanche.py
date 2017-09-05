vS_entrada = input().split()
codigo = int(vS_entrada[0])
qtd = int(vS_entrada[1])
f_total = 0
if (codigo == 1): f_total = 4*qtd
elif (codigo == 2):	f_total = 4.50*qtd
elif (codigo == 3):	f_total = 5*qtd
elif (codigo == 4):	f_total = 2*qtd
elif (codigo == 5):	f_total = 1.50*qtd
print("Total: R$ %.2f" % f_total)