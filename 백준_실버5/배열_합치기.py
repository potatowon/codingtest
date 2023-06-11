import sys
from collections import deque
n, m = map(int, input().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()
A = deque(A)
B = deque(B)
answer = []
while A and B:
    a = A.popleft()
    b = B.popleft()
    if a >= b:
        answer.append(b)
        A.appendleft(a)
    else:
        answer.append(a)
        B.appendleft(b)


if A:
    for i in A:
        answer.append(i)
elif B:
    for j in B:
        answer.append(j)

print(answer)
