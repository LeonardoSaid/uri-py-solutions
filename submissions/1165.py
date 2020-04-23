n = int(input())

while n > 0:
    x = int(input())
    
    c = 0
    
    for i in range(2, (x//2)+1):
        if x % i == 0:
            c += 1
            break

    if c == 1:
        print("%d nao eh primo" % x)
    else:
        print("%d eh primo" % x)
        
    n -= 1