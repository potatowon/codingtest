import sys

n = int(input())
seats = input()
cnt = 0
stack = []

for s in seats:
    if s == 'S':
        cnt += 1
    elif s == 'L':
        if stack and stack[-1] == 'L':
            stack.pop()
            cnt += 1
        elif stack == []:
            stack.append(s)
cnt += 1

if len(seats) <= cnt:
    print(len(seats))
else:
    print(cnt)
