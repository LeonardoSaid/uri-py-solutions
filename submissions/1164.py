n = int(input())

while n > 0:
    x = int(input())
    
    c = 0
    
    for i in range(1, (x//2)+1):
        if x % i == 0:
            c += i

    if c == x:
        print("%d eh perfeito" % x)
    else:
        print("%d nao eh perfeito" % x)
        
    n -= 1