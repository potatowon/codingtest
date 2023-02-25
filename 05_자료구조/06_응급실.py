'''
환자가 도착한 순서대로 진료/ 단 위급상황시 빨리 초치

- 접수한 순서대로 뽑기
- 위험도가 높은 환자 존재하면 제일 뒤로 보낸다.

1. n, m
2. 위험도

m 번째 환자가 진료받는지 출력
'''

from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
numbers = deque(map(int, sys.stdin.readline().split()))

# n, m = 5, 2
# numbers = [60, 50, 70, 80, 90]
q = deque()
for idx, num in enumerate(numbers):
    q.append((num, idx))
cnt = 1 # 진료 순서

while True:
    tmp = q.popleft()       # 차트의 가장 앞의 환자
    if tmp[0] < max(q)[0]:     # 위험도가 더 높은 환자가 있다면 맨 뒤로 이동
        q.append(tmp)
        # cnt += 1
    else:
        if tmp[1] == m:     # m 번째 인경우 멈추고 cnt 반환
            break
        else:
            cnt += 1        # 위험도가 높은 사람이 없고, m 번째도 아니면 계속 진료
print(cnt)



'''
max 함수의 특징 만약 list의 요소들이 튜플등으로 들어가있다면 가장 맨 앞의 원소를 기준으로 찾는다.
'''