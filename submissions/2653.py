n = list()

while True:
    
    try:
        
        
        
        j = input()
        
        if(n.count(j) == 0):
            n.append(j)
        
        
    
    
    except EOFError:
        break
    
print(len(n))