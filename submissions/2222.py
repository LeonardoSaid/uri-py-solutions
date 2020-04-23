for t in range(int(input())):
    
    listaConjunto = list()
    
    for n in range(int(input())):
        vec = 0
        c = map(int, input().split()[1:])
        for i in c:
            vec = vec | (1 << (i-1))
        
        listaConjunto.append(vec)
        
        
    for n in range(int(input())):
        op, x, y = map(int, input().split())
        
        if op == 1:
            print(bin(listaConjunto[x-1]&listaConjunto[y-1]).count('1'))
        else:
            print(bin(listaConjunto[x-1]|listaConjunto[y-1]).count('1'))
        
        