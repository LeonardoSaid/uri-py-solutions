while True:
    try:
        n = int(input())
        m = 12
        while n > 0:
            x = float(input())
            if x < m:
                m = x
            n -= 1
        print('%.2f' % m)
        
    except EOFError:
        break