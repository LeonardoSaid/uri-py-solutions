def fat(n):
  if n == 0: return 1
  if n == 1: return 1
  return n*fat(n-1)

while True:
    n = input()
    if n == '0': break
    acm = 0
    l = len(n)
    for i in n:
      acm += int(i)*fat(l)
      l -= 1
    print(acm)