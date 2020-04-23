while True:
    
    x,y = map(int, input().split())
    
    if x+y == 0:
        break
    
    r = 0
    c = y-x
    
    if c // 100 > 0:
        r += c // 100
        c -= (c // 100)*100
        
    if c // 50 > 0:
        r += c // 50
        c -= (c // 50)*50
        
    if c // 20 > 0:
        r += c // 20
        c -= (c // 20)*20
        
    if c // 10 > 0:
        r += c // 10
        c -= (c // 10)*10
        
    if  c // 5 > 0:
        r += c // 5
        c -= (c // 5)*5
        
    if c // 2 > 0:
        r += c // 2
        c -= (c // 2)*2

    if r != 2 or c != 0:
        print('impossible')
    else:
        print('possible')