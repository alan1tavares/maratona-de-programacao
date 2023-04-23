v_int_entrada = [int(input()), int(input())]
int_val = min(v_int_entrada) + 1
int_soma = 0
for c in range(int_val, max(v_int_entrada)):
	if( not(c%2 == 0) ):
		int_soma += c
print(int_soma)