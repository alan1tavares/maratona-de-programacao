numeroTeste = int(input())
alfabeto =['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
for x in range(0,numeroTeste):
    string = input()
    stringReverse = string[::-1]
    if(string == stringReverse):
        for y in range(0, len(alfabeto)):
            string = string.replace(alfabeto[y], "")
        if (string == ""):
            print ("yes")
        else:
            print("no")
    else:
        print("no")
