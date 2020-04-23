n = int(input())

while n > 0:
    
    x,y,z = map(str,input().split())
    
    if int(x) < 10:
        x = '0'+x
    if int(y) < 10:
        y = '0'+y
    if z == '1':
        asd = 'abriu'
    else:
        asd = 'fechou'
    
    
    
    print('%s:%s - A porta %s!' % (x,y,asd))
    
    
    
    n -= 1