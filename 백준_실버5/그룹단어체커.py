import sys

t = int(input())
cnt = t
for _ in range(t):
    word = sys.stdin.readline().rstrip()
    stack = []
    for i in word:
        if not stack:
            stack.append(i)
        elif stack and stack[-1] != i:
            if i in stack:
                cnt -= 1
                break
            else:
                stack.append(i)
print(cnt)