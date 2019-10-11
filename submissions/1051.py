x = float(input(""))

if x <= 2000.0:
  print("Isento")

elif x <= 3000.0:
  salario = ( x - 2000.0 ) * 0.08
  print("R$ %.2f" % salario)

elif x <= 4500:
  salario = 0.08*1000 + ( x - 3000 ) * 0.18
  print("R$ %.2f" % salario)

else:
  salario = 0.08*1000 + 0.18*1500 + ( x - 4500 ) * 0.28
  print("R$ %.2f" % salario)