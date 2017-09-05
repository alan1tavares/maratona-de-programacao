s_tipo1 = input()
s_tipo2 = input()
s_tipo3 = input()

if(s_tipo3 == "carnivoro"):
	print("aguia")

elif(s_tipo3 == "onivoro"):
	if(s_tipo2 == "ave"):
		print("pomba")
	elif(s_tipo2 == "mamifero"):
		print("homem")
	else:
		print("minhoca")

elif(s_tipo3 == "herbivoro"):
	if(s_tipo2 == "mamifero"):
		print("vaca")
	else:
		print("lagarta")
else:
	if(s_tipo2 == "inseto"):
		print("pulga")
	else:
		print("sanguessuga")