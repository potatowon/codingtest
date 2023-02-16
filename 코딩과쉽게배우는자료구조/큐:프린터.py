'''
중요도가 높은 문서를 먼저 인쇄하는 프린터 개발
중요도순서가 담긴 배열, 내가 요청한 문서는 무엇인지
-> 요청한 문서가 언제 인쇄되는지 return
'''
from collections import deque

def solution(priorities, location):
    Q = deque([(pri, idx) for pri, idx in zip(priorities, range(len(priorities)))])
    print(Q)
    answer = 0
    while Q:
        tmp = Q.popleft()
        if any(tmp[0] < q[0] for q in Q):
            Q.append(tmp)
        else:
            answer += 1
            if tmp[1] == location:
                return answer
        

            

