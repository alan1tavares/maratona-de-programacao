notas = input().split();
f_media = float(notas[0])*2 + float(notas[1])*3 + float(notas[2])*4 + float(notas[3])*1
f_media = f_media/(2+3+4+1)
print("Media: %.1f" % f_media)
if(f_media>=7.0):
	print("Aluno aprovado.")
elif(f_media<5.0):
	print("Aluno reprovado.")
else:
	print("Aluno em exame.")
	nota_exame = float(input())
	print("Nota do exame: %.1f" % nota_exame)
	f_media_final = (nota_exame+f_media)/2
	if(f_media_final >= 5.0):
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")
	print("Media final: %.1f" % f_media_final)