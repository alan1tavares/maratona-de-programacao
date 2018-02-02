nCasos = int(input())
for i in range(1, nCasos+1):
    alunos = list(map(int, input().split()))
    alunos = sorted(alunos)
    print('Case {}: {}'.format(i, alunos[len(alunos)-1]))