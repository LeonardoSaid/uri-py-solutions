n = int(input())

while n > 0:
    
    x = int(input())
    
    if 2014 - x < 0:
        print('%d A.C.' % abs(2014-x))
    else:
        print('%d D.C.' % (2015-x))
    
    n -= 1