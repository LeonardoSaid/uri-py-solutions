import math
x,y = map(int, input().split())
m = list()

for i in range(1, 10):
    m.append(str(math.ceil((x*y)*(i/10))))

print(' '.join(m))
