cont = 0
soma = 0
while True:

  if(cont == 2):
    break

  x = float(input())

  if x < 0 or x > 10:
    print("nota invalida")
  else:
    cont += 1
    soma += x

print("media = %.2f" % (soma/2))