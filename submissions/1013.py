a,b,c = map( int, input().split())

d = (a+b+abs(a-b)) / 2

print("%d eh o maior" % ((c+d+abs(c-d)) / 2))