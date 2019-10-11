h1, m1, h2, m2 = map(int, input().split())

duracao = ((h2*60)+m2)-((h1*60)+m1)
if duracao <= 0:
  duracao += 24*60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracao // 60, duracao - 60*(duracao // 60)))