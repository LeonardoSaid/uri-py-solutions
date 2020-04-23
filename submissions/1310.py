while True:
    try:
        
        n = int(input())
        custoPorDia = int(input())
        
        receitas = []
        
        while n:
            receitas.append(int(input())-custoPorDia)
            n -= 1
        
        maior = menor = receitas[0]
        for i in receitas[1:]:
            menor = max(i, menor + i)
            maior = max(maior, menor)
        
        if maior < 0:
            maior = 0
        print(maior)

    except EOFError:
        break