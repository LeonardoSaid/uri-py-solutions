n = input()

dic = { 
  '61' : 'Brasilia',
  '71' : 'Salvador',
  '11' : 'Sao Paulo',
  '21' : 'Rio de Janeiro',
  '32' : 'Juiz de Fora',
  '19' : 'Campinas',
  '27' : 'Vitoria',
  '31' : 'Belo Horizonte'
 }

if n in dic.keys():
   print(dic[n])
else:
  print("DDD nao cadastrado")