f_lado = list(map(float, input().split()))
exp1 = abs(f_lado[1] - f_lado[2]) < f_lado[0] and f_lado[0] < f_lado[1] + f_lado[2]
exp2 = abs(f_lado[0] - f_lado[2]) < f_lado[1] and f_lado[1] < f_lado[0] + f_lado[2]
exp3 = abs(f_lado[0] - f_lado[1]) < f_lado[2] and f_lado[2] < f_lado[0] + f_lado[1]
if(exp1 and exp2 and exp3):
	perimetro = f_lado[0] + f_lado[1] + f_lado[2]
	print("Perimetro = %.1f" % perimetro)
else:
	area = ((f_lado[0]+f_lado[1]) * f_lado[2]) / 2
	print("Area = %.1f" % area)