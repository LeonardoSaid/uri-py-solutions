while True:
  n,m = input().split()

  if n == m == '0':
    break

  n = int(n)
  m = int(m)

  original = []

  for x in range(int(n)):
        original.append(input())
  
  a,b = input().split()
  a = int(a)
  b = int(b)

  scaleA = int(a/n)
  scaleB = int(b/m)

  nova = []

  for i in original:
      r = ''
      for j in i:
            r += j * scaleB
      for j in range(scaleA):
            nova.append(r)

  for i in nova:
        print(i)

  print()
