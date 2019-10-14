n = float(input())

if n <= 400:
  print("Novo salario: %.2f" % (n*(1+0.15)))
  print("Reajuste ganho: %.2f" % abs(n - n*(1+0.15)))
  print("Em percentual: %d %%" % 15)
elif n <= 800:
  print("Novo salario: %.2f" % (n*(1+0.12)))
  print("Reajuste ganho: %.2f" % abs(n - n*(1+0.12)))
  print("Em percentual: %d %%" % 12)
elif n <= 1200:
  print("Novo salario: %.2f" % (n*(1+0.10)))
  print("Reajuste ganho: %.2f" % abs(n - n*(1+0.10)))
  print("Em percentual: %d %%" % 10)
elif n <= 2000:
  print("Novo salario: %.2f" % (n*(1+0.07)))
  print("Reajuste ganho: %.2f" % abs(n - n*(1+0.07)))
  print("Em percentual: %d %%" % 7)
else:
  print("Novo salario: %.2f" % (n*(1+0.04)))
  print("Reajuste ganho: %.2f" % abs(n - n*(1+0.04)))
  print("Em percentual: %d %%" % 4)