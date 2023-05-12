n_Pi = int(input())
Pi = list(map(int, input().split()))
mountain = [0]*n_Pi

for idx, p in enumerate(Pi):
    if idx > 0:
        mountain[idx] = p - Pi[idx-1]

stack = []

for m in mountain:
    if m > 0 and stack[-1] > 0:
        n = stack.pop()
        stack.append(n+m)
    else:
        stack.append(m)

if all(i <= 0 for i in mountain):
    print(0)
else:
    print(max(stack))
