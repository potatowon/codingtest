n, k = map(int, input().split())

num = list(input().rstrip())
stack = []
cnt = 0
for i in num:

    while stack and (int(stack[-1]) < int(i)) and cnt < k :
        stack.pop()
        # stack.append(i)
        cnt += 1
    stack.append(i)



print(''.join(stack[:(n-k)]))