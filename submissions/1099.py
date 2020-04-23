def soma(x, y):
  asd = 0
  if x > y:
    aux = x
    x = y
    y = aux
  
  for i in range(x+1, y):
      if i % 2 == 1:
          asd += i
  return asd

n = int(input())

while n > 0:
  x, y = map(int, input().split())
  print(soma(x,y))

  n-= 1