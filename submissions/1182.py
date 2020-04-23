n = int(input())
t = input()

c = 0

for i in range(12):
    for j in range(12):
        x = float(input())
        if j == n:
            c += x

if t == 'S':
    print("%.1f" % c)
else:
    print("%.1f" % (c/12))