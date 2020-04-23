n = int(input())
asd = list()

s = input().split()

for i in s:
  asd.append(int(i))

print("Menor valor: %d" % min(asd))
print("Posicao: %d" % (asd.index(min(asd))) )