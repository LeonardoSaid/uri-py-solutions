def isPrimo(num):
  for i in range(2, (int( num ** (1/2)) )+1  ):
    if num % i == 0:
        return False
  return True

n = int(input())
while n > 0:
    x = int(input())
    if isPrimo(x):
      print("Prime")
    else:
      print("Not Prime")
    n -= 1