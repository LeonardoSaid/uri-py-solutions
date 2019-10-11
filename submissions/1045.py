s = input("").split()
a = float(s[0])
b = float(s[1])
c = float(s[2])

if ((b > a)and(b > c)):
  aux = a;
  a = b;
  b = aux;
elif ((c > a)and(c > b)):
  aux = a;
  a = c;
  c = aux;

if (c > b):
    aux = b;
    b = c;
    c = aux;

if (a>= b+c):
      print("NAO FORMA TRIANGULO");
elif((a*a) == (b*b)+(c*c)):
      print("TRIANGULO RETANGULO");
elif((a*a) > (b*b)+(c*c)):
      print("TRIANGULO OBTUSANGULO");
elif((a*a) < (b*b)+(c*c)):
      print("TRIANGULO ACUTANGULO");

if ((a == b)and(b == c)):
      print("TRIANGULO EQUILATERO");
elif ((a == b)or(a == c)or(b == c)):
        print("TRIANGULO ISOSCELES");