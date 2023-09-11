from collections import deque

numbers = deque(input().rstrip())
N = 0
while numbers:
    N += 1
    str_N = deque(str(N))
    while str_N and numbers:
        curr = str_N.popleft()
        num = numbers.popleft()
        if curr == num:
            pass
        else:
            numbers.appendleft(num)




print(N)