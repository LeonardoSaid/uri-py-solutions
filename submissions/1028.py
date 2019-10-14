def mdcAux(x, y):
    if (x%y == 0):
        return y
    else:
        return mdcAux(y,x % y)

n = int(input())

while n > 0:
  f1, f2 = map(int, input().split())
  if f2 > f1:
        aux = f1
        f1 = f2
        f2 = aux
  print(mdcAux(f1, f2))
  n -= 1