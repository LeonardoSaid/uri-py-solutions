def conta(n1,n2):
    ct = 0
    for i in range(0, len(n2)):
        if n1 == n2[i:i+len(n1)]:
            ct += 1
    return ct

c = 1
while True:
    try:
        n1 = input()
        n2 = input()
        
        print('Caso #%d:' % c)
        if conta(n1,n2) == 0:
            print('Nao existe subsequencia')
        else:
            if conta(n1,n2) > 1:
                print('Qtd.Subsequencias: %d' % conta(n1,n2))
                print('Pos: %d' % (n2.rfind(n1)+1))
            else:
                print('Qtd.Subsequencias: %d' % conta(n1,n2))
                print('Pos: %d' % (n2.find(n1)+1))
        print()
        
        c += 1
        
    except EOFError:
        break