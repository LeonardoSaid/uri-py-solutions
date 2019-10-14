n = int(input())

a = n // 365
n -= 365*a

m = n // 30
n -= 30*m

print("%d ano(s)" % a)
print("%d mes(es)" % m)
print("%d dia(s)" % n)