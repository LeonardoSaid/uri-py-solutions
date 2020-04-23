t = int(input())

while t > 0:
    
    pa,pb,g1,g2 = map(float, input().split())
    
    c = 0
    
    while pa <= pb:
        pa = int((pa*(g1/100))+pa)
        pb = int((pb*(g2/100))+pb)
        c += 1
        
        if c > 100:
            break
    
    if(c > 100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % c)
    
    t -= 1
    