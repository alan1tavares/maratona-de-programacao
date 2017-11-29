nConsultas = int(input())
while(nConsultas != 0):
    n, m = map(int, input().split())

    for i in range(0, nConsultas):
        x, y = map(int, input().split())
        if(x < n and y > m):
            print('NO')
        elif(x > n and y > m):
            print('NE')
        elif(x > n and y < m):
            print('SE')
        elif(x < n and y < m):
            print('SO')
        else:
            print('divisa')

    nConsultas = int(input())
