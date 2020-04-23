n = int(input())
c = int(input())

m = list()

while c > 0:
    
    x = int(input())
    
    if x not in m:
        m.append(x)
    
    c -= 1
    
print(n-len(m))