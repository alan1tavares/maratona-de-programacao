int_ls = list(map(int, list(input().split())))
a = int_ls[0]
i = 1
while int_ls[i] <= 0:
	i += 1
n = int_ls[i]
int_ls = list(range(a, n+a))
print(sum(int_ls))