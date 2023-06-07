stack = []
answer = 0
S = input().rstrip()

for i in S:
    if stack and stack[-1] != i:
        answer += 0.5

    stack.append(i)

print(int(answer + 0.5))