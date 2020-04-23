x = [int(input())]

print("N[0] = %d" % (x[0]))

for i in range(1, 10):
  x.append(x[i-1]*2)
  print("N[%d] = %d" % (i, x[i]))
