def conveteBase(num,base):
   convertString = "0123456789ABCDEF"
   if num < base:
      return convertString[num]
   else:
      return conveteBase(num//base,base) + convertString[num%base]

numeroInstancias = int(input())
saida = ""
for x in range(0, numeroInstancias):
    entrada = int(input())  
    for i in range (2, 17):
        if(i == 10):
            pass
        num = conveteBase(entrada, i)
        if(num == num[::-1]):
            saida += str(i) + " "
    if(saida == ""):
        print("-1")
    else:
        print(saida[:len(saida)-1])
    saida = ""