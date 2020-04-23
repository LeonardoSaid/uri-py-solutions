x = list()

for i in range(20):
  x.append(int(input()))

x = x[::-1]

for i in range(0,len(x)):
  print("N[%d] = %d" % (i, x[i]))