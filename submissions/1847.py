a,b,c = map(int, input().split())
    
if b < a:
        if c >= b:
            print(':)')
        elif c < b and (b-c) < (a-b):
            print(':)')
        elif c < b and (b-c) >= (a-b):
            print(':(')
elif b > a:
        if c <= b:
            print(':(')
        elif c > b and (b-a) > (c-b):
            print(':(')
        elif c > b and (b-a) <= (c-b):
            print(':)')
else:
        if b < c:
            print(':)')
        else:
            print(':(')