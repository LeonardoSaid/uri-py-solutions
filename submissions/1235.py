n = int(input(""))

for i in range(0,n):

  v = input()
  aux = int(len(v)/2) -1
  s = v[aux::-1] + v[len(v)-1:aux:-1]
  print(s)
  
  