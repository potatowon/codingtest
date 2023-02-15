'''
수 N 개가 주어졌을 때, i 부터 j 수까지의 합을 구하는 프로그램을 만드시오

answer = S(j) - S(i-1)
'''

import sys

n, m = map(int, sys.stdin.readline().split(' '))
numbers = list(map(int, sys.stdin.readline().split(' ')))
prifix_sum = [0]
tmp = 0

for i in numbers:
    tmp += i
    prifix_sum.append(tmp)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split(' '))
    print(prifix_sum[j]-prifix_sum[i-1])

