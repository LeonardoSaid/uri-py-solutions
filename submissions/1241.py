n = int(input(""))

for i in range(0,n):

  v = input().split()
  result = v[0].find(v[1])

  if(result == -1):
    print('nao encaixa')
  elif(result+len(v[1]) == len(v[0])):
    print('encaixa')
  else:
    print('nao encaixa')