def primo(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**(1/2))+1 ):
        if(n % i == 0):
            return False
    return True
    
while True:
    try:
        s = input()
        r = 'Nada'
        if primo(int(s)):
            for i in s:
                if primo(int(i)):
                    pass
                else:
                    r = 'Primo'
                    break
            if r == 'Nada':
                r = 'Super'
        print(r)
    
    except EOFError:
        break