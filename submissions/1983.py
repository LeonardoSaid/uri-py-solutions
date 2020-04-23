n = int(input())

m = 0
mm = 0

while n > 0:
    
    s = input().split()
    
    if (float(s[1]) > m):
        m = float(s[1])
        mm = s[0]
    
    
    n -= 1

if m < 8:
    print('Minimum note not reached')
else:
    print(mm)