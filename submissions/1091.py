while True:

  k = int(input())

  if k == 0:
    break

  n,m = map(int, input().split())

  while k > 0:

    x,y = map(int, input().split())

    if x == n or y == m:
      print("divisa")
    elif x > n:
      if y > m:
        print("NE")
      else:
        print("SE")
    else:
      if y > m:
        print("NO")
      else:
        print("SO")

    k -= 1