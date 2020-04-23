def led(digit):
  if digit == '0' or digit == '6' or digit == '9':
    return 6
  elif digit == '2' or digit == '3' or digit == '5':
    return 5
  elif digit == '1':
    return 2
  elif digit == '4':
    return 4
  elif digit == '7':
    return 3
  elif digit == '8':
    return 7

n = int(input())

while n > 0:
  soma = 0
  v = input()
  for i in v:
    soma += led(i)
  print("%d leds" % soma)
  n -= 1