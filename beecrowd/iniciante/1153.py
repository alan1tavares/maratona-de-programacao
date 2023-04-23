n = int(input())
fatorial = n
for x in range(1,n):
    fatorial *= (n-x)
print(fatorial)