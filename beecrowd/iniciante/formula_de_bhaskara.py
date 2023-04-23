import math

float_3 = input().split()
a = float(float_3[0])
b = float(float_3[1])
c = float(float_3[2])
delta = (b**2)-4*a*c

if(delta<0):
	print("Impossivel calcular")
else:
	r1 = -b+math.sqrt(delta)
	r2 = -b-math.sqrt(delta)
	if(r1 == 0 or r2 == 0):
		print("Impossivel calcular")
	else:
		r1 = r1/(2*a)
		r2 = r2/(2*a)
		print("R1 = %.5f" % r1)
		print("R2 = %.5f" % r2)