f_entrada = input().split()
x = float(f_entrada[0])
y = float(f_entrada[1])

if(x==0==y):
	print("Origem")
elif(x==0):
	print("Eixo Y")
elif(y==0):
	print("Eixo X")
elif(x > 0 and y >0):
	print("Q1")
elif(x < 0 and y < 0):
	print("Q3")
elif(x > 0):
	print("Q4")
else:
	print("Q2")