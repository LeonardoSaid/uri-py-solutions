n =int(input())
i = 1
t=[1]
while i < n:
    if i == 1:
        t.append(i)
    elif i > 1:
        aux = t[i-2] + t[i-1]
        t.append(aux)
        
    i = i + 1
    
    
    
    
t = t[::-1]
for j in range(0, n):
    t[j] =str(t[j])
t = ' '.join(t)
print(t)