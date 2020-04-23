def conta(a, n):
   soma = 0
   for i in range(0,n):
     soma += (a+i)
   return soma

s = input().split()

aa = int(s[0])

for i in range(1, len(s)):
  if int(s[i]) > 0:
    bb = int(s[i])
    break

print(conta(aa,bb))