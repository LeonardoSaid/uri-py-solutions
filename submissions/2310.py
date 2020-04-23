n = int(input())

saque = list()
blo = list()
ata = list()

while n > 0:
    n -= 1
    nome = input()
    s,b,a = map(int, input().split())
    s1,b1,a1 = map(int, input().split())
    
    saque.append((s, s1))
    blo.append((b, b1))
    ata.append((a, a1))

# total, suc
m1 = [0, 0]
m2 = [0, 0]
m3 = [0, 0]

for i,j,k in zip(saque, blo, ata):
    m1[0] += i[0]
    m1[1] += i[1]
    m2[0] += j[0]
    m2[1] += j[1]
    m3[0] += k[0]
    m3[1] += k[1]
    
print('Pontos de Saque: %.2f %%.' % ((m1[1]/m1[0])*100))
print('Pontos de Bloqueio: %.2f %%.' % ((m2[1]/m2[0])*100))
print('Pontos de Ataque: %.2f %%.' % ((m3[1]/m3[0])*100))

