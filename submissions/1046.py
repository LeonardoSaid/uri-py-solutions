a,b = map(int, input().split())

x = (24 - a) + b

if(x>24):
    x = abs(24 - (24-a+b))

print("O JOGO DUROU %d HORA(S)" % x )