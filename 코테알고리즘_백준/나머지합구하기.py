'''
백준 온라인 저지 10986 번 골드3


N개의 수가 주어졌을때 연속된 부분의 합이 M 으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오

자연수 나머지의 정리

r(A) = a
r(B) = b
A = xn + a
B = yn + b
r(A-B) = r(n(x-y)+a-b) = a-b


따라서
r(A) = 0
r(B) = 0

r(A-B) = 0


(A_i + ... + A_j)%M == 0 이라함은

(S[j]-S[i-1])% M== 0
1) S[j]%M == 0 , S[i-1] == 0 이거나
2) S[j]%M == S[i-1]%M 인경우

'''

import sys

n, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
divisor = [0]*m
# 구간 합 배열

prefix_sum = [0]*n
prefix_sum[0] = A[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + A[i]
# print(prefix_sum)
cnt = 0
# 나머지가 0인 경우의 수
for i in prefix_sum:
    r = i%m
    if r == 0:
        cnt += 1
    divisor[r] += 1

# 나머지가 같은 경우의 수 -> 나머지가 같은 인덱스에서 중복 허용안하고 2개 뽑기 (combination)

for j in divisor:
    if j > 1:
        cnt += (j*(j-1))//2
print(cnt)