a = input("").split()
a[0] = float(a[0])
a[1] = float(a[1])
a[2] = float(a[2])
print("TRIANGULO: %.3f" % ((a[0]*a[2])/2))
print("CIRCULO: %.3f" % (3.14159*(a[2]*a[2])))
print("TRAPEZIO: %.3f" % (((a[0]+a[1])*a[2])/2))
print("QUADRADO: %.3f" % (a[1]*a[1]))
print("RETANGULO: %.3f" % (a[0]*a[1]))