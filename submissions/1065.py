c = 0
for i in range(5):
  x = int(input())
  if x % 2 == 0:
    c += 1
print("%d valores pares" % c)