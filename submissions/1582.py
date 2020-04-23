import math

def mdc(x,y,z):
  return mdcAux(x, mdcAux(y, z))

def mdcAux(x, y):
    if (x%y == 0):
        return y
    else:
        return mdcAux(y,x % y)

def a(x,y,z):
  s = (y**2) + (z**2)
  if(s == x**2):
    return True
  else:
    return False

def b(x,y,z):
  s = (x**2) + (z**2)
  if(s == y**2):
    return True
  else:
    return False

def c(x,y,z):
  s = (x**2) + (y**2)
  if(s == z**2):
    return True
  else:
    return False

while True:
  try:
    p1, p2, p3 = map(int, input().split())
    if mdc(p1,p2,p3) == 1 and (a(p1,p2,p3) or b(p1,p2,p3) or c(p1,p2,p3)):
      print("tripla pitagorica primitiva")
    elif a(p1,p2,p3) or b(p1,p2,p3) or c(p1,p2,p3):
      print("tripla pitagorica")
    else:
      print("tripla")

  except EOFError:
    break