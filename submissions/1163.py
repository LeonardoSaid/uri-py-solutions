import math

while True:
  try:
    g = 9.80665
    pi = 3.14159
    h = float(input())
    p1, p2 = map(int, input().split())
    n = int(input())
    while n > 0:
      alpha, v = map(float, input().split())
      alpha = alpha * pi / 180.0
      sx = v*math.cos(alpha)
      sy = v*math.sin(alpha)
      z = g*h / (v*v)
      t = (v / g) * (math.sin(alpha) + math.sqrt(math.sin(alpha) * math.sin(alpha) + 2 * z))
      x = sx * t
      if(x >= p1 and x <= p2):
        print("%.5f -> DUCK" % x)
      else:
        print("%.5f -> NUCK" % x)
      n -= 1



  except EOFError:
    break