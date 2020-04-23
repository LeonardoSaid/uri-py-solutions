x,y = map(int, input().split())
s = list(map(int, input().split()))

res = 'YOU WIN'

for a,b in zip(s, s[1:]):
    if abs(a-b) > x:
        res = 'GAME OVER'
        break

print(res)