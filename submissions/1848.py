n = 3
while n > 0:
    soma = 0
    
    while True:
        s = input()
        if s == 'caw caw':
            print(soma)
            break
        else:
            s = s.replace('*', '1')
            s = s.replace('-', '0')
            soma += int(s,2)
    
    n -= 1