s = input()

c = 0
nc = 0

for i in range(12):
    for j in range(12):
        x = float(input())
        
        if i > 6 and j < i and j > (11-i):
            c += x
            nc += 1
            
if s == 'S':
    print("%.1f" % (c))
else:
    print("%.1f" % (c/nc))