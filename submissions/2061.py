x,y = map(int, input().split())

while y > 0:
    
    s = input()
    
    if s == 'fechou':
        x += 1
    else:
        x -= 1
    y -= 1
print(x)