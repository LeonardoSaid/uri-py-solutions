x,y = map(int, input().split())
div = divmod(x,abs(y))
if y < 0:
    print(-div[0], div[1])
else:
    print(div[0], div[1])