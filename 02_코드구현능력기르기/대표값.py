'''N명의 학생의 수학점수, 학생들의 평균(소수 첫째 반올림), 평균에 가장 가까운 학생은 몇번째 인덱스인지 출력'''

import sys
# input
N = int(input())
scores = list(map(int, sys.stdin.readline().split()))
avg = int((sum(scores)/N) + 0.5)
# 합산
sort_score = sorted(scores, key=lambda x: abs(x-avg))

for idx in range(len(sort_score)):
    if abs(avg - sort_score[idx]) == abs(avg -sort_score[idx-1]):
        sort_score[idx-1], sort_score[idx] = max(sort_score[idx], sort_score[idx-1]), min(sort_score[idx], sort_score[idx-1])
idx = scores.index(sort_score[0])+1

print(avg, idx)
''' round 는 round_half_even 방식을 취한다
따라서 4.500 -> 4가 나와버린다.. -> 정확하게 절반에 있으면 짝수 값으로 반올림해버린다 
예를 들어 5.5000 의 경우는 짝수인 6
4.50000 인경우는 짝수 4로 반올림을 한다...

따라서 round 함수를 사용하지 말고 +0.5를 사용하는 방식을 이용한다.'''
## 최솟값 구하기

# N = int(input())
# scores = list(map(int, sys.stdin.readline().split()))
# avg = round(sum(scores)/N)
#
# min =3423432423
#
# for idx, x in enumerate(scores):
#     tmp = abs(x - avg)
#     if tmp < min:
#         min = tmp
#         score = x
#         res = idx + 1
#     elif tmp == min:
#         if x > score:
#             score = x
#             res = idx+1

