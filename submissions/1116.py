n = int(input())

while n > 0:
  x, y = map(float, input().split())
  if y == 0:
    print("divisao impossivel")
  else:
    print("%.1f" % (x/y))

  n-= 1