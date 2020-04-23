# my solution couldn't solve on time so i had to resort to other methods
# credits to https://www.geeksforgeeks.org/k-fibonacci-series/
def kfib(N, K) : 
    Array = [0] * (N + 1)
    
    if (N <= K) : 
        print(N-1)
        return
      
    i = 0
    sm = int(((K-1)*K)/2)
      
    for i in range(0, K):
        Array[i] = i
          
    Array[i+1] = sm

    for i in range(K+1, N+1):
        Array[i] = sm-Array[i-K-1]+Array[i-1]
        sm = Array[i]

    print(Array[N-1] % 1000007)

for i in range(int(input())):
    k,n = map(int, input().split())
    
    if n < k:
        print((n-1)%1000007)
    else:
        kfib(n,k)
        
        