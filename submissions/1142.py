n = int(input())

c = 0

for i in range(n):
  for j in range(3):
    c += 1
    print("%d " % c, end="")
  print("PUM")
  c += 1