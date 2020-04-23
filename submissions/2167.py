n = int(input())
r = list(map(int, input().split()))

q = 0

for atual,ant in zip(r[1:], r):
    if atual < ant:
        q = r.index(atual)+1
        break
    
    
print(q)