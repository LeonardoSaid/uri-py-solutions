def numRollsToTarget(d: int, f: int, t: int) -> int:
        
        dp = [[0] * (t+1) for _ in range(d+1)]
        dp[0][0] = 1
        
        for i in range(1, d+1):
            for j in range(1, t+1):
                dp[i][j] = sum(dp[i-1][j-k] for k in range(1, f+1) if j-k >= 0)
                
        return dp[-1][-1] % (10**9 + 7)

n = int(input())

for i in range(n):
  s,d = map(int, input().split())
  print("%.15f" % ((numRollsToTarget(d, 6, s))/(6**d)))