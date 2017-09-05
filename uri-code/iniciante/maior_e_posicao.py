int_maior = int(input())
int_posicao = 1
for c in range(2, 101):
	int_val = int(input())
	if ( int_val > int_maior ):
		int_maior = int_val
		int_posicao = c
print(int_maior)
print(int_posicao)