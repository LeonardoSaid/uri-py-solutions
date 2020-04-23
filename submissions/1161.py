import math

def fat(n):
  if n == 0: return 1
  if n == 1: return 1
  return n*fat(n-1)

while True:
    try:
      a, b = map(int, input().split())
      print(fat(a)+fat(b))
    except EOFError:
        break