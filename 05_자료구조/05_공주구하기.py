'''
N 명의 왕자 -> 나이순

K 외치면 제외 원밖으로 -> 구구단
'''
from collections import deque
n, k = map(int, input().split())
# n, k = 8, 3
num = deque(range(1, n+1))
while len(num) > 1:                 # num 값이 1명 남을 때까지 반복 ( 아래 과정을 )
    for _ in range(k-1):            # 맨 앞을 k-1번 pop 하여 뒤에 위치 -> k 번째가 맨 앞에 위치한다.
        num.append(num.popleft())
    num.popleft()                   # 맨 앞의 요소를 Pop 한다.

print(num[0])


# while num:


