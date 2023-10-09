'''
합이 최대가 되는 경로를 구하라
'''
import sys

n = int(input())
dp = [[0]*i for i in range(1, n+1)]
ta = []
for _ in range(n):
    ta.append(list(map(int, sys.stdin.readline().split())))

dp[0][0] = ta[0][0]

for i in range(1, n):
    for j in range(len(ta[i])):
        if j == 0:
            dp[i][j] = ta[i][j] + dp[i-1][j]

        elif j == len(ta[i]) -1:
            dp[i][j] = ta[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = ta[i][j] + max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[n-1]))