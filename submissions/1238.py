n = int(input(""))

for i in range(0,n):

  v = input().split()
  s = ""

  if(len(v[0]) < len(v[1])):
    k = len(v[0])
  else:
    k = len(v[1])

  for i in range(k):
    s += (v[0][i])
    s += (v[1][i])

  if(len(v[0]) < len(v[1])):
    s += v[1][slice(len(v[0]), len(v[1]))]
  else:
    s += v[0][slice(len(v[1]), len(v[0]))]
  
  print(s)