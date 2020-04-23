x = int(input())

while True:
  z = int(input())
  if z > x:
    break

n = x
nc = 1

while n < z:
  x += 1
  n += x
  nc += 1

print(nc)