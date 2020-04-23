x = int(input())
y = int(input())

c = 0

if x > y:
  aux = x
  x = y
  y = aux

for i in range(x+1, y):
  if i % 2 == 1:
    c += i
print(c)