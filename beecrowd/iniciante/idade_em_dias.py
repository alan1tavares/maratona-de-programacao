idade_dias = int(input());

ano = int(idade_dias/365)
print("%d ano(s)" % ano)
mes = int((idade_dias%365)/30)
print("%d mes(es)" % mes)
dia = int((idade_dias%365)%30)
print("%d dia(s)" % dia)