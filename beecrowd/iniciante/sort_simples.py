entrada = input().split()
int_list = list(map(int, entrada))
int_list.sort()
for x in int_list:
	print(x)
print()
for x in entrada:
	print(x)