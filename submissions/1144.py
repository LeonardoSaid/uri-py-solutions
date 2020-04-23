n = int(input())
i = 1
c = 1
while c <= 2*n:
  if c % 2 == 1:
    print("%d %d %d" % (i, i**2, i**3))
  else:
    print("%d %d %d" % (i, (i**2)+1, (i**3)+1))
    i += 1
  c += 1