import math
while True:
    n = int(input())
    
    if n == 0:
        break
    
    m = list()
    
    for i in range(n):
        mm = list()
        for j in range(n):
            mm.append(0)
        m.append(mm)
        
    m[0][0] = 1
    
    for i in range(0, n):
        if i >= 1:
            m[i][0] = m[i-1][0]*2
            
        for j in range(1, n):
            m[i][j] = m[i][j-1]*2
                
    
    t = len(str(m[n-1][n-1]))
    
    for i in range(n):
        for j in range(n):
            
            m[i][j] = str(m[i][j])
            
            while len(m[i][j]) < t:
                
                m[i][j] = ' ' + m[i][j]
                
        asd = ' '.join(m[i])
        
        print(asd)
    print()