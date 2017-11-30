testCase = int(input())

for x in range(1, testCase + 1):
    tamanhoCampo = input()
    campo = input()
    campo = campo.replace('.#', '1')
    print("Case " + str(x) + ": " + str(campo.count('1')))
