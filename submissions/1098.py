a = 0
while a <=2:

  if a ==0 or a == 1 or a ==2:
    print("I=%.0f J=%.0f" % (a, 1+a))
    print("I=%.0f J=%.0f" % (a, 2+a))
    print("I=%.0f J=%.0f" % (a, 3+a))
  else:
    print("I=%.1f J=%.1f" % (a, 1+a))
    print("I=%.1f J=%.1f" % (a, 2+a))
    print("I=%.1f J=%.1f" % (a, 3+a))

  
  a = round(a+ 0.2,2)