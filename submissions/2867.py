x = int(input())

while x > 0 :
    
    n,m = map(int, input().split())
    
    print(len(str(n**m)))
    
    x -= 1