def money(soma, bill):
  count = 0
  while soma >= bill:
    soma = round(soma - bill, 2)
    count += 1
  return count

a = [100, 50, 20, 10, 5, 2, 1]

v = float(input())
print("%d" % v)
for i in a:
  x = money(v, i)
  v -= x*i
  v = round(v,2)
  print("%d nota(s) de R$ %.0f,00" % (x, i))