numeroTeste = int(input())
#alfabeto =['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
alfabeto = ['B','C', 'D', 'E', 'F', 'G', 'J','K','L', 'N', 'P','Q','R','S','Z']
for x in range(0,numeroTeste):
    string = input()
    for i in range(0, len(alfabeto)):
        string = string.replace(alfabeto[i], " ");
    string = string.split()
    print (string)
    maior = 0
    for i in range(0, len(string)):
        if (string[i] == string[i][::-1] and len(string[i]) > maior):
            maior = len(string[i])
        else:

    print (maior)
def a(string):
    lista = []
    stringReverse = string[::-1]
    for i in range(0, len(string)):
        for j in range(0, len(string)):
            if(string[i] == stringReverse[j]):
