x,y = map(int, input().split())
cgeral = 1
c = 1

while cgeral <= y:
  l = list()
  
  while c <= x and cgeral <= y:
    l.append(str(cgeral))
    cgeral += 1
    c += 1
  
  c = 1
  print(' '.join(l))
  
  