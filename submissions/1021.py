def money(soma, bill):
  count = 0
  while soma >= bill:
    soma = round(soma - bill, 2)
    count += 1
  return count

a = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

v = float(input())
print("NOTAS:")
for i in a:
  x = money(v, i)
  v -= x*i
  v = round(v,2)
  if i >= 2:
    print("%d nota(s) de R$ %.2f" % (x, i))
  else:
    if i == 1:
      print("MOEDAS:")
    print("%d moeda(s) de R$ %.2f" % (x, i))