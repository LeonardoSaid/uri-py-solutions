n = int(input())

while n > 0:
  a,b,c = map(float, input().split())

  print("%.1f" % ( (a*2 + b*3 + c*5) / 10 ))

  n-=1