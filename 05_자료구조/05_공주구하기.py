'''
N 명의 왕자 -> 나이순

K 외치면 제외 원밖으로 -> 구구단
'''
from collections import deque
n, k = int(input().split())
# n, k = 8, 3
num = deque([i for i in range(1, n+1)])
while num:
    num.rotate(-(k-1))
    answer = num.popleft()

print(answer)


# while num:


