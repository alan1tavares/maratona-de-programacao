entrada = list(map(int, input().split()))
score = list(map(int, input().split()))
contador = 0
for i in range(entrada[0]):
    if(score[i] >= score[entrada[1]-1] and score[i] > 0):
        contador += 1
print("\n"+str(contador))
