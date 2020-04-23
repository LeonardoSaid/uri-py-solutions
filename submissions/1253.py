n = int(input(""))

for i in range(0,n):

  s  = input()
  k = int(input())
  v = ""

  for j in range(len(s)):   
    x = (ord(s[j]))

    if (x-k) < 65:
     x = 90 - (64 - (x-k))
    else:
      x -= k

    v += str(chr(x))
  
  print(v)