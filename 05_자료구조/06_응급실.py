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
# n, m = map(int, sys.stdin.readline().split())
# numbers = deque(map(int, sys.stdin.readline().split()))

n, m = 6, 0
numbers = deque([60, 60, 90, 60, 60])
stack = []
rt = 0
tmp = numbers.popleft()
if tmp < max(numbers):
    numbers.append(tmp)
    stack.append(tmp)