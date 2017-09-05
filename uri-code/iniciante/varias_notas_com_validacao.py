def calcular_media():
	str_saida = ""
	float_nota = ""
	while True:
		float_entrada = float(input())
		if( float_entrada >= 0 and float_entrada <= 10):
			if( float_nota == "" ):
				float_nota = float_entrada
			else:
				media = (float_nota + float_entrada)/2
				str_saida += str("media = %.2f" % media)
				break
		else:
			str_saida += "nota invalida\n"
	print(str_saida)

int_opcao = 1
while True:
	if(int_opcao == 1):
		calcular_media()
	elif(int_opcao == 2):
		break
	print("novo calculo (1-sim 2-nao)")
	int_opcao = int(input())