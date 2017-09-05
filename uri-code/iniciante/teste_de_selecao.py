int_4 = input().split()
a = int(int_4[0])
b = int(int_4[1])
c = int(int_4[2])
d = int(int_4[3])
soma_cd = c+d
soma_ab = a+b
if((b > c and d > a) and soma_cd > soma_ab and c*d > 0 and a%2==0):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")