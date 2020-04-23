k = int(input())

while k > 0:

  n = int(input())
  i = 0
  t=[]

  while i <= n:
      if i == 0 or i == 1:
          t.append(i)
      
      if i > 1:
          aux = t[i-2] +t[i-1]
        
          t.append(aux)
      i = i + 1

  print("Fib(%d) = %d" % (n, t[len(t)-1]))

  k -= 1
