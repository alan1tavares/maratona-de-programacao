n = input()
a = n
if (not(a=="")):
    for x in range(0, len(n)):
        a = a.replace("()","")
    if(a ==""):
        print("possible")
    elif (len(a) == 2):
        print("possible")
    else:
        print("impossible")
else:
    print("impossible")
