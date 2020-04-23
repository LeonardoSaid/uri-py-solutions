import math

while True:
  try:
    a, b, c = map(float, input().split())
    PI = 3.141592654
    m = (b * math.tan((a * PI) / 180.0) + c) * 5;
    print("%.2f" % m)
    
  except EOFError:
    break