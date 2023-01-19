'''
자연수 N, K 가 주어졌을때 N의 약수들 중 K 번째로 작은 수를 출력하시오
'''

# def solution(N, K):
#     result = []
#     for i in range(1, N+1):
#         if N%i == 0:
#             result.append(i)
#     if len(result) < K :
#         return -1
#     else:
#         return result[K-1]
#
# print(solution(6, 3))

import sys

N, K = map(int, sys.stdin.readline().split())
result = []
for i in range(1, N + 1):
    if N % i == 0:
        result.append(i)
if len(result) < K:
    print(-1)
else:
    print(result[K - 1])


