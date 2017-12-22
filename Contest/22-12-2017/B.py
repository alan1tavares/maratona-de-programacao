from itertools import permutations
for x in range(int(input())):
    permLista = permutations(sorted(list(input())))
    for h in list(permLista): 
        print(''.join(h))
    print()