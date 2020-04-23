while True:
    try:
        
        n = int(input())
        
        lesmas = list(map(int, input().split()))
        
        if max(lesmas) < 10:
            print(1)
        elif max(lesmas) < 20:
            print(2)
        else:
            print(3)

    
    except EOFError:
        break