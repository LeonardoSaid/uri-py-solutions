n = int(input())

while n > 0:
    
    s = input().split()
    
    x,y = map(int, input().split())
    
    if (x+y) % 2 == 0:
        print(s[s.index('PAR')-1])
    else:
        print(s[s.index('IMPAR')-1])
    
    
    n -= 1