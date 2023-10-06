import sys

n = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)] # n번째 까지의 경우 최솟값을 구해낸다.

dp[0] = cost[0] # 첫 번째 집은 아무거나 선택가능

for i in range(1, n):
    dp[i][0] = cost[i][0] + (min(dp[i-1][1], dp[i-1][2]))
    dp[i][1] = cost[i][1] + (min(dp[i-1][0], dp[i-1][2]))
    dp[i][2] = cost[i][2] + (min(dp[i-1][1], dp[i-1][0]))

print(min(dp[n-1]))
