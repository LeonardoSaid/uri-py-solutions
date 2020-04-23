s,t,f = map(int, input().split())
    
if (s+t+f) > 24:
        print(s+t+f-24)
elif (s+t+f) < 0:
        print(s+t+f+24)
else:
        print(s+t+f)