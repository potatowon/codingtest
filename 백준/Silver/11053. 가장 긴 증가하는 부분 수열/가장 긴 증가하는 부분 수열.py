# memoization 을 활용한 방법 ai
import sys
N = int(input())

dp = [0]*(N+1)
a = [0] + list(map(int, sys.stdin.readline().split()))

for i in range (1, N+1):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
