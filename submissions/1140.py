while True:
  s = input().upper().split()
  
  if s[0] == '*':
    break
  
  c = ord(s[0][0])

  asd = 'Y'

  for i in s:
    if ord(i[0][0]) == c:
      pass
    else:
      asd = 'N'