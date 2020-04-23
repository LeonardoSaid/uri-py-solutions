while True:
    try:
        
        n = int(input())
        
        m = list()
        
        for i in range(0,n):
            mm = list()
            for j in range(0,n):
                if i == j:
                    mm.append(2)
                elif (i+j) == n-1:
                    mm.append(3)
                else:
                    mm.append(0)
                
            m.append(mm)
        
        for i in range(n//3, n-n//3 ):
            for j in range(n//3 ,n-n//3 ):
                m[i][j] = 1
        
        m[n//2][n//2] = 4
        
        
        for i in range(n):
            print(''.join(str(x) for x in m[i]))
        print()
    
    except EOFError:
        break