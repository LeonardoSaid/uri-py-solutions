while True:
  x = int(input())

  if x == 0:
    break
  
  a = list()

  for i in range(1,x+1):
    a.append(str(i))
  
  print(' '.join(a))