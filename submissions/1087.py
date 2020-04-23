soma = -1
while(soma != 0):
  s = input("").split()
  x1= int(s[0])
  y1= int(s[1])
  x2= int(s[2])
  y2= int(s[3])
  soma = x1+x2+y1+y2
  
  if(soma == 0):
    break
  
  if x2 == x1 and y2 == y1:
    print(0)
  elif x2 == x1 or y2 == y1:
    print(1)
  elif(abs(x1 - x2) == abs(y1 - y2)):
    print(1)
  else:
    print(2)