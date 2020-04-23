def mdcAux(x, y):
    if (x%y == 0):
        return y
    else:
        return mdcAux(y,x % y)

while True:
  p = list()
  n, m = map(int, input().split())
  
  if(n+m == 0): 
    break

  for i in range(0, n):
    s = input().split()
    p.append(int(s[m-1]))

  soma = 0

  for i in range(0,n):
    soma += p[i]
  
  for i in range(0,n):
    x = p[i]
    if(x):
      g = mdcAux(x, soma)
      print("%d / %d" % (int(x/g), int(soma/g)))
    else:
      print("0 / 1")