str_saida = ""
while(True):
	str_entrada = input()
	if ( str_entrada == "2002" ):
		str_saida += "Acesso Permitido"
		break
	else:
		str_saida += "Senha Invalida\n"
print( str_saida )