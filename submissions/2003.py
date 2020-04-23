while True:
    try:
        s = input().split(':')
        
        
        sec = ((int(s[0])*60 + int(s[1]))+60)-(8*60)
        
        if sec <= 0:
            print('Atraso maximo: 0')
        else:
            print('Atraso maximo: %d' % sec)
        
    
    except EOFError:
        break