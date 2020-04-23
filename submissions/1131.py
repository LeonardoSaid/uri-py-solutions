dic = {
  'I' : 0,
  'G' : 0,
  'E' : 0,
  'n' : 0
}

while True:

  i, g = map(int, input().split())

  if i == g:
    dic['E'] += 1
  elif i > g:
    dic['I'] += 1
  else:
    dic['G'] += 1

  dic['n'] += 1


  print("Novo grenal (1-sim 2-nao)")
  x = input()
  if x == '2':
    break

print("%d grenais" % dic['n'])
print("Inter:%d" % dic['I'])
print("Gremio:%d" % dic['G'])
print("Empates:%d" % dic['E'])

if dic['I'] == dic['G']:
  print("Nao houve vencedor")
elif dic['I'] > dic['G']:
  print("Inter venceu mais")
else:
  print("Gremio venceu mais")