while True:
    
    x = int(input())
    
    if x == 0:
        break
    
    soma = 0
    
    if x % 2 == 1:
        x += 1
    
    for i in range(x, x+10, 2): soma += i
    print(soma)