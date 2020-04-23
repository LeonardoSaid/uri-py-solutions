k = int(input())

while k > 0:

  m = int(input())
  p =list(map(int, input().split()))
  sp = sorted(p, reverse= True)

  c = 0

  for i in range(len(p)):
    if p[i] != sp[i]:
      c += 1
  
  print(m-c)
  
  k -= 1