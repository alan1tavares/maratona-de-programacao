i = 0
while i <= 2 :
	for j in range(1, 4):
		if( i - round(i) == 0.0 ):
			print ("I=%d J=%d" % (i, (j+i)))
		else:
			print ("I=%.1f J=%.1f" % (i, (j+i)))
	i+=0.2
	i = round(i,1)