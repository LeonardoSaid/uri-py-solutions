n = int(input())

while n > 0:

  x,y = map(int, input().split())
  
  c = 0

  if(x % 2 == 1):
    c += x
    y -= 1
  else:
    x += 1
    c += x
    y -= 1
  for i in range(y):
    x += 2
    c += x

  print(c)

  n -= 1