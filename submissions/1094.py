n = int(input())

db = {
  'C' : 0,
  'R' : 0,
  'S' : 0,
  'T' : 0
}

while n > 0:
  s = input().split()
  
  db[s[1]] += int(s[0])
  db['T'] += int(s[0])
  n -= 1

print("Total: %d cobaias" % db['T'])
print("Total de coelhos: %d" % db['C'])
print("Total de ratos: %d" % db['R'])
print("Total de sapos: %d" % db['S'])
print("Percentual de coelhos: %.2f %%" % ( (db['C']/db['T'])*100  ))
print("Percentual de ratos: %.2f %%" % ( (db['R']/db['T'])*100  ))
print("Percentual de sapos: %.2f %%" % ( (db['S']/db['T'])*100  ))