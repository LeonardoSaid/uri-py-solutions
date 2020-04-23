soma = 0
c = 1
for i in range(1, 40, 2):
  soma += (i/c)
  c *= 2

print("%.2f" % soma)