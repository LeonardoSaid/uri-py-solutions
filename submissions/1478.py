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
        
    for i in range(n):
        c = 1
        for j in range(i, n):
            m[i][j] = c
            m[j][i] = c
            c += 1
                
    
    for i in range(n):
        tx = ''
        for j in range(n):
            tx += " %3d" %m[i][j]
        print(tx[1:])
    print("")