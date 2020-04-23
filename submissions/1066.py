a = 0
b = 0
c = 0
d = 0

for i in range(5):
  
  x = int(input())

  if x > 0:
    c += 1
  elif x < 0:
    d += 1
  
  if x % 2 == 0:
    a += 1
  else:
    b += 1
  
print("%d valor(es) par(es)" % a )
print("%d valor(es) impar(es)" % b )
print("%d valor(es) positivo(s)" % c )
print("%d valor(es) negativo(s)" % d )