n = int(input())

par = list()
impar = list()

while n > 0:

  x = int(input())

  if x % 2 == 1:
    impar.append(x)
  else:
    par.append(x)

  n -= 1
    
impar = sorted(impar, reverse= True)
par = sorted(par)

for i in par:
  print(i)
for i in impar:
  print(i)