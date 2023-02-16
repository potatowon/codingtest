'''
연속적으로 답을 맞히는 경우 가산점
연속 k 번 맞을 경우 k 점

시험문제의 채점 결과가 주어졌을 떄 총 점수를 계산하는 프로그램을 작성하시오
'''

import sys

N = int(input())
score = list(map(int, sys.stdin.readline().split()))
total_score = 0
cnt = 1
for s in score:
    if s == 1:
        total_score += cnt
        cnt += 1
    if s == 0:
        cnt = 1
print(total_score)
