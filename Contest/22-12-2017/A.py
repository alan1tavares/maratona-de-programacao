import fileinput as fl
for linha in fl.input():
    pessoas = 'ABC'
    linha = linha.replace(' ', '')
    if(linha.count('1') == 1):
        print(pessoas[linha.find('1')])
    elif(linha.count('0') == 1):
        print(pessoas[linha.find('0')])
    else:
        print('*')