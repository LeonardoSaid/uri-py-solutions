c = 0
d = 0
n = int(input())

while n > 0:
  x = int(input())
  if x >= 10 and x <= 20:
    c += 1
  else:
    d += 1
  n -= 1

print("%d in" % c)
print("%d out" % d)