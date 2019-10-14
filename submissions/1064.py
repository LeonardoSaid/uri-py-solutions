c = 0
d = 0
for i in range(6):
  n = float(input())
  if n > 0:
    c += 1
    d += n

print("%d valores positivos" % c)
print("%.1f" % (d/c))