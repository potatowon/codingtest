# 동적계획법 예시
import sys
dp = [0]*10001

N = int(input())
wines = [0] * 10001
for i in range(1, N+1):
    wines[i] = int(sys.stdin.readline())

dp[1] = wines[1]
dp[2] = wines[1] + wines[2]


# def drink(x): # x 번째의 최댓값
#     if x == 1 or x == 2 or x == 3:
#         return dp[x]
#     if dp[x] != 0:
#         return dp[x]
#     dp[x] = max((drink(x-2) + wines[x]), (drink(x-3) + wines[x-1] + wines[x]), (drink(x-1)))
#     return dp[x]
# # 재귀로 풀면 깊이 에러 발생 --> 바텀업 방식 사용하자
# print(drink(N))

for i in range(3, N+1):
    dp[i] = max((dp[i-2] + wines[i]), (dp[i-3] + wines[i-1] + wines[i]), (dp[i-1]))

print(dp[N])