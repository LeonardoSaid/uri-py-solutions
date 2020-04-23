c = 0
nc = 0

while True:

  x = float(input())

  if x >= 0 and x <= 10:
    c += x
    nc += 1
    if nc == 2:
      print("media = %.2f" % (c/2))
      while x != 1 and x != 2:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
      if x == 2:
        break
      else:
        c = 0
        nc = 0
  else:
    print("nota invalida")