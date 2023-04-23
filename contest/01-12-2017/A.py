val1, val2 = map(int, input().split())
if(val1%val2 ==0 or val2%val1 ==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
