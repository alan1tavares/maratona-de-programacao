int_n = int(input())
int_n += 1
for c in range(2, int_n,2):
	print( "%d^2 = %d" % (c, (c**2)) )