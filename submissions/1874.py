while True:
    h,p,f = map(int, input().split())
    
    if h+p+f == 0:
        break
    
    m = list()
    
    for i in range(h):
        line = list(map(int, input().split()))
        m.append(line)
        
    ff = list(map(int, input().split()))
    
    
    for x in ff:
        i = h-1
        j = p-1
        
        while (j >= 0):
            if i < 0:
                i = h-1
                j -= 1
            
            if m[i][j] == 0:
                m[i][j] = x
                break
            
            i -= 1
    
    for i in m:
        print(' '.join(str(x) for x in i))