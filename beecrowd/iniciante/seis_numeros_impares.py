int_entrada = int(input())
int_c = 0
while(int_c < 6):
	if(not(int_entrada%2 == 0)):
		print(int_entrada)
		int_c += 1
	int_entrada += 1