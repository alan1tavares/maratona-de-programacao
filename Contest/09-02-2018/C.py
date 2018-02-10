tabela, x = map(int, input().split())
count = 0
for a in range(1, tabela+1):
    if(x % a == 0 and x / a <= tabela):
        count +=1
print (count)
