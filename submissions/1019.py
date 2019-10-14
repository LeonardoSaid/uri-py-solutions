n = int(input())

h = n // (60**2)
n -= h*60**2

m = n // 60
n -= m*60

print("%d:%d:%d" % (h,m,n))