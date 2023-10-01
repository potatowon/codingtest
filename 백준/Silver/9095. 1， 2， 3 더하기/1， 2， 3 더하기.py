dp = [0]*1001

dp[1] = 1
dp[2] = 2
dp[3] = (1 + dp[1] + dp[2])
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])