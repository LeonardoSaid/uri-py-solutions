import math
while True:
    n = int(input())
    
    if n == 0:
        break
    
    m = list()
    
    for i in range(n):
        mm = list()
        for j in range(n):
            mm.append(1)
        m.append(mm)
    
    for i in range(1, math.ceil(n/2) ):
        for x in range(i, n-i):
            for y in range(i, n-i):
                m[x][y] += 1
                
    
    for i in range(n):
        tx = ''
        for j in range(n):
            tx += " %3d" %m[i][j]
        print(tx[1:])
    print("")