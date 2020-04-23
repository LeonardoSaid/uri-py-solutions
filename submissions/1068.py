while True:
  try:
    s = input()

    p = list()
    ans = 'correct'

    for c in s:
      if c == '(':
        p.append('(')
      elif c == ')':
        if not p:
          ans = 'incorrect'
        else:
          p.pop()
    
    if p:
      print('incorrect')
    else:
      print(ans)

  except EOFError:
    break