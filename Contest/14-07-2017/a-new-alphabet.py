#line = input();
table = {
    "a": "@",
    "b": 8,
    "c": "(",
    "d": "|)",
    "e": 3,
    "f": "#",
    "g": 6,
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "[]\/[]",
    "n": "[]\[]",
    "o": 0,
    "p": "|D",
    "q": "(,)",
    "r": "|Z",
    "s": "$",
    "t": "']['",
    "u": "|_|",
    "v": "\/",
    "w": "\/\/",
    "x": "}{",
    "y": "`/",
    "z": 2
}

entrada = input().lower();
saida = ""
for x in range(0, len(entrada)):
    if (entrada[x] in table):
        saida += str(table[entrada[x]])
    else:
        saida += entrada[x]

print (saida)
