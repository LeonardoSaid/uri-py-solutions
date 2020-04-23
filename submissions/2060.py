n = int(input())

d = {
    2:0,
    3:0,
    4:0,
    5:0
}

s = list(map(int,input().split()))

for i in s:
    if i % 2 == 0:
        d[2] += 1
    
    if i % 3 == 0:
        d[3] += 1
    
    if i % 4 == 0:
        d[4] += 1
    
    if i % 5 == 0:
        d[5] += 1

print("%d Multiplo(s) de 2" % d[2])
print("%d Multiplo(s) de 3" % d[3])
print("%d Multiplo(s) de 4" % d[4])
print("%d Multiplo(s) de 5" % d[5])