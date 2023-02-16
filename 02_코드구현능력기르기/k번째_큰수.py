'''
1-100 사이의 자연수가 적힌 카드 N 장 -> 중복 허용
이중 3장을 뽑아 각 카드에 적힌 수의 합을 기록
기록한 값 중 K 번째로 큰 수

N, K
N의 카드값
'''

# 3장을 뽑아 합산  -> 큰수 연산(중복을 허용하여 뽑는다)-> 콤비네이션

# 내림차순 [0:3], [1:4], [2:5],...,[K-1:K+2]
import sys
import itertools

N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = list(itertools.permutations(numbers, 3))
result.sort(reverse=True, key=lambda x: sum(x))
answer = []
for idx in range(len(result)):
    answer.append(sum(result[idx]))
a = set(answer)
answer = list(a)
answer.sort(reverse=True)
print(answer[K-1])


''' 모듈 사용안하고 풀이 하기'''

# N, K = map(int, sys.stdin.readline().split())
# numbers = list(map(int, sys.stdin.readline().split()))
# res = set()
#
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             res.add(a[i] + a[j] + a[k])
# res = list(res)
# res.sort(reverse=True)
# print(res[k-1])

# print(a)