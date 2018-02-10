n, a = map(int, input().split())
tiras = sorted(list(map(int, input().split())))
for i in reversed(range(len(tiras))):
    if(i-1 > len(tiras) and tiras[i] == tiras[i-1]):
        continue
    tiras[i] -= 1
    a -= len(tiras) - i