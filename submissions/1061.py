w1 = int(input().split()[1])

s1 = input()
x1 = int(s1.split()[0])
y1 = int(s1.split()[2])
z1 = int(s1.split()[4])

w2 = int(input().split()[1])
s2 = input()
x2 = int(s2.split()[0])
y2 = int(s2.split()[2])
z2 = int(s2.split()[4])

sec1 = (w1*24*60*60) + (x1*60*60 + y1*60 + z1)
sec2 = (w2*24*60*60) + (x2*60*60 + y2*60 + z2)

res = sec2 - sec1

dias = res // (24*60*60)
res -= (dias * (24*60*60))
horas = res // (60*60)
res -= (horas * (60*60))
minutos = res // (60)
res -= (minutos * 60)

print("%d dia(s)" % dias)
print("%d hora(s)" % horas)
print("%d minuto(s)" % minutos)
print("%d segundo(s)" % res)