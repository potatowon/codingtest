'''
최대한 많은 부서의 부품

-> 금액보다 많은 지원금

d : 신청한 지원금
budget : 예산

그리디

오름차순 정렬
'''

def solution(d, budget):
    d.sort()
    cnt = 0
    for m in d:
        if budget >= m:
            budget -= m
            cnt +=1
    return cnt

print(solution([1,3,2,5,4], 9))
