alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
    try:
        n = int(input())
        
        while n > 0:
            
            s = input()
            print(alf[((len(s.split())-1)*3)+s.split()[0].count('.')-1])
            
            n -= 1
    except EOFError:
        break