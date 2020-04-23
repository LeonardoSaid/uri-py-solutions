n = int(input())

d = {
    1001: 1.5,
    1002: 2.5,
    1003: 3.5,
    1004: 4.5,
    1005: 5.5
}

c = 0 


while n > 0:
      
    x,y = map(int, input().split())
    c += y*d[x]
    n -= 1

print("%.2f" % c)