while True:
    s = list(map(int,input().split()))
    if s[0] == 0:
        break
    
    print(int((((s[0]*s[1])*100) / s[2])**(1/2)))