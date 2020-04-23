import itertools

def tri(a,b,c):
    if abs(b-c) < a and a < b+c:
        if abs(a-c) < b and b < a+c:
            if abs(a-b) < c and c < a+b:
                return True
    return False

s = list(map(int, input().split()))
s = list(itertools.combinations(s, 3))

t = False

for i in s:
    if tri(i[0], i[1], i[2]):
        t = True
        break

if t:
    print('S')
else:
    print('N')
    