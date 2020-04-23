n = int(input(""))

for i in range(0,n):

  cont = 0
  k = int(input())
  
  for j in range(k):
    s = input()
    for x in range(len(s)):
      cont += (ord(s[x])-65) + j + x
  
  print(cont)
  

  