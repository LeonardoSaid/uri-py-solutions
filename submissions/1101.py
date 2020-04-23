while True:
  x, y = map(int, input().split())

  if x <=0 or y <= 0:
    break
  
  if x > y:
    aux = x
    x = y
    y = aux
  
  soma = 0

  for i in range(x, y+1):
    print("%d "% i, end="")
    soma += i
  print("Sum=%d" % soma)