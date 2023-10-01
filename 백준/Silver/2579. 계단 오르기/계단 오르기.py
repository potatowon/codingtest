import sys

n = int(input())
stair = [0] + [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * 1001
dp[1] = stair[1]
if n > 1:  # n이 1보다 클 때만
    dp[2] = stair[1] + stair[2]

    for i in range(3, n + 1):
        dp[i] = max((dp[i-3] + stair[i-1] + stair[i]), (dp[i-2] + stair[i]))

print(dp[n])
