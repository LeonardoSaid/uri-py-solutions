n =int(input())

k = 0
fibonot = 0
fib1 = 3
fib2 = 5

while k < n:
    for i in range(fib1+1, fib2):
      if(k >= n):
        break
      else:
        k += 1
        fibonot = i
    
    aux = fib2+fib1
    fib1 = fib2
    fib2 = aux

print(fibonot)