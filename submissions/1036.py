s = input("").split()
a = float(s[0])
b = float(s[1])
c = float(s[2])

x = (b*b) - (4*a*c);

if x > 0 and a != 0:
  x = x**(1/2)
  r1 = (-b+x)/(2*a);
  r2 = (-b-x)/(2*a);

  print("R1 = %.5lf"% r1);
  print("R2 = %.5lf"% r2);
  
else:
  print("Impossivel calcular")