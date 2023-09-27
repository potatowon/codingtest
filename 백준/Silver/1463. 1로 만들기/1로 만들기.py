# import sys
#
# limit_number = 15000
# sys.setrecursionlimit(limit_number)
#
#
# memoization = [-1]*10000001
# memoization[1] = 0
# memoization[2], memoization[3] = 1, 1
# def dp(x):
#     # 이미 계산된 값은 바로 반환
#     if memoization[x] != -1:
#         return memoization[x]
#
#     res = dp(x-1) + 1
#     if x % 2 == 0:
#         res = min(res, dp(x//2)+ 1)
#     if x % 3 == 0:
#         res = min(res, dp(x//3)+1)
#
#     memoization[x] = res
#     return res
#
# n = int(input())
# print(dp(n))

## 재귀말고 메모이제이션만 사용하자
dp = [-1]*1000001
dp[1], dp[2], dp[3] = 0, 1, 1

n = int(input())
for x in range(4,n+1):
    if dp[x] != -1:
        continue
    res = dp[x-1] + 1
    if x % 2 == 0:
        res = min(res, dp[x//2]+1)
    if x % 3 == 0:
        res = min(res, dp[x//3]+1)
    dp[x] = res

print(dp[n])





