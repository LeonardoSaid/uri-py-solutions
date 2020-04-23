n = 0
nc = 0
while True:
  z = int(input())
  if z < 0:
    break
  
  n += z
  nc += 1

print("%.2f" % (n/nc))
