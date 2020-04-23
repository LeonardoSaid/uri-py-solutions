import math

def count(n):
  ans = 0
  acc = 1
  while acc <= n:
    a = n - acc + 1
    b = 2*acc
    ans += a // b * acc
    ans += min(a % b, acc)
    acc = 2* acc
  return ans

def getAns(a,b):
  return count(b) - count(a-1)

while True:
    try:
      a,b = map(int, input().split())
      print(getAns(a,b))
    except EOFError:
        break