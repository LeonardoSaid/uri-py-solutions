dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        
        x,y = map(int, input().split())
        
        if x == 12 and y == 24:
            print('E vespera de natal!')
        elif x == 12 and y == 25:
            print('E natal!')
        elif x == 12 and y > 25:
            print('Ja passou!')
        else:
            falta = 0
            for i in range(x, 12):
                falta += dias[i-1]
            falta += 25 - y
            print('Faltam %d dias para o natal!' % (falta))
        
        
    except EOFError:
        break