int_n = int(input())
str_saida = ""
for c in range(0, int_n):
	int_intervalo = list(map(int, input().split()))
	int_soma = sum([i for i in range(min(int_intervalo)+1, max(int_intervalo)) if not(i%2 == 0)])
	str_saida += str("%d\n" % int_soma)
print(str_saida[:len(str_saida)-1])