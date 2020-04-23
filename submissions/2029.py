pi = 3.14
while True:
    try:
        v = float(input())
        d = float(input())
        
        print('ALTURA = %.2f' % (v/(pi*(d/2)**2))) 
        
        print('AREA = %.2f' % (pi*(d/2)**2))
        
    except EOFError:
        break