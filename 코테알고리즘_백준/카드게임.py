'''
실버5 2164

1번카드가 맨위 n 번카드가 맨 아래 있다 

1. 맨 위 카드를 바닥에 버린다.
2. 그 다음 가장 위 카드를 가장 아래로 옮긴다.
3. 위 과정을 반복하여 가장 마지막에 남는 카드를 구하는 프로그램을 작성
'''

'''
덱의 형태를 떠올려야 하므로 deque 를 사용하여 문제를 접근하자
'''
from collections import deque
import sys

n = int(sys.stdin.readline())
dq = deque(range(1, n+1))

while len(dq) > 1:
    dq.popleft()
    a = dq.popleft()
    dq.append(a)

print(*dq)





