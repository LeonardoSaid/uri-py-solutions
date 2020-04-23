n = int(input())

d = dict()

while n > 0:

  x = int(input())

  if x not in d.keys():
    d[x] = 1
  else:
    d[x] += 1

  n -= 1


for key in sorted(d.keys()):
  print("%d aparece %d vez(es)" % (key, d[key]))